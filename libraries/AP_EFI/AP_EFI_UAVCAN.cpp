/*
   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */
#include <AP_HAL/AP_HAL.h>
#if HAL_WITH_UAVCAN

#include "AP_EFI_UAVCAN.h"
#include <AP_BoardConfig/AP_BoardConfig_CAN.h>

extern const AP_HAL::HAL &hal;




AP_EFI_UAVCAN::AP_EFI_UAVCAN(AP_EFI &_frontend, uint8_t _instance):
    AP_EFI_Backend(_frontend, _instance)
{
    if (AP_BoardConfig_CAN::get_can_num_ifaces() >= 1) {
        for (uint8_t i = 0; i < MAX_NUMBER_OF_CAN_DRIVERS; i++) {
            if (hal.can_mgr[i] != nullptr) {
                AP_UAVCAN* uavcan = hal.can_mgr[i]->get_UAVCAN();

                if (uavcan != nullptr) {
                    uint8_t listener_channel = uavcan->register_efi_listener(this, get_uavcan_node_id());
                    _manager = i;
                    hal.console->printf("AP_EFI_UAVCAN: EFI Listener registered to channel %d\n", listener_channel);
                } 
            }
        }
    }
}

AP_EFI_UAVCAN::~AP_EFI_UAVCAN()
{
    if (hal.can_mgr[_manager] != nullptr) {
        AP_UAVCAN *ap_uavcan = hal.can_mgr[_manager]->get_UAVCAN();
        if (ap_uavcan != nullptr) {
            ap_uavcan->remove_efi_listener(this);
        }
    }
}
void AP_EFI_UAVCAN::update()
{
    // TODO: should I be using semaphores here? Should it be blocking?
    // Referred to compass/rangefinder/baro
    if (_sem->take_nonblocking()) {
        copy_to_frontend();
        _sem->give();
    }
}

void AP_EFI_UAVCAN::handle_efi_msg(const EFI_State& message_efi_state)
{
    if (_sem->take_nonblocking()) {
        copy_state(message_efi_state, _internal_state);
        _sem->give();
    }
}


#endif //HAL_WITH_UAVCAN
