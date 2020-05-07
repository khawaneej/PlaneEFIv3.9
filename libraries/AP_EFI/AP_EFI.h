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

#pragma once



#include <AP_Common/AP_Common.h>
#include <AP_Param/AP_Param.h>
#include <AP_SerialManager/AP_SerialManager.h>
#include "AP_EFI_Backend.h"
#include "AP_EFI_State.h"

/*
 * This library aims to read data from Electronic Fuel Injection 
 * or Engine Control units. It is focused around the generic
 * internal combustion engine state message provided by the 
 * UAVCAN protocol due to its comprehensiveness, but is extensible
 * to use other forms of data transfer besides UAVCAN. 
 * 
 *
 *
 * Authors: Sriram Sami and David Ingraham
 * With direction from Andrew Tridgell, Robert Lefebvre, Francisco Ferreira and
 * Pavel Kirienko.
 * Thanks to Yonah, SpektreWorks Inc, and HFE International.
 */

class AP_EFI {
public:
    friend class AP_EFI_Backend;

    // For parameter initialization
    AP_EFI();

    // Initializes backends based on parameters
    void init(AP_SerialManager &serial_manager);

    // Requests all backends to update the frontend. Should be called at 10Hz.
    void update();
    
    uint8_t num_instances() const { return _backend_count; };

    // Returns full state of a particular backend instance
    EFI_State* get_state(uint8_t instance) { return &_state[instance]; };

    static bool is_healthy(const EFI_State& state);

    // Parameter info
    static const struct AP_Param::GroupInfo var_info[];

    // Backend driver types
    enum EFI_Communication_Type {
        EFI_COMMUNICATION_TYPE_NONE   = 0,
        EFI_COMMUNICATION_TYPE_UAVCAN = 1,
        EFI_COMMUNICATION_TYPE_SERIAL_MS = 2
    };

protected:

    // Back end Parameters
    struct {
      AP_Int8 _uavcan_node_id;
      AP_Float _coef1;
      AP_Float _coef2;
    } param[EFI_MAX_INSTANCES];

    EFI_State _state[EFI_MAX_INSTANCES];

private:
    // Front End Parameters
    AP_Int8 _enabled;
    AP_Int8 _type[EFI_MAX_INSTANCES];

    // Tracking backends
    AP_EFI_Backend* _backends[EFI_MAX_BACKENDS];
    uint8_t _backend_count; // number of registered EFIs

    
};
