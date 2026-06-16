#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#   GIMP - The GNU Image Manipulation Program
#   Copyright (C) 2026 Sergio Maya
#
#
#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation; either version 3 of the License, or
#   (at your option) any later version.

import sys

import gi
gi.require_version('Gimp', '3.0')
from gi.repository import Gimp
gi.require_version('GimpUi', '3.0')
from gi.repository import GimpUi

from gi.repository import GLib

class MyFirstPlugin (Gimp.PlugIn):
    def do_query_procedures(self):
        return [ "plugin-automatization" ]

    def do_set_i18n (self, name):
        return False

    def do_create_procedure(self, name):
        procedure = Gimp.ImageProcedure.new(self, name,
                                            Gimp.PDBProcType.PLUGIN,
                                            self.run, None)

        procedure.set_image_types("*")

        procedure.set_menu_label("Automatization")
        procedure.add_menu_path('<Image>/Filters')

        procedure.set_documentation("Automatization comic pages",
                                    "Automatization comic pages",
                                    name)
        procedure.set_attribution("Maya López", "Sergio", "2026")

        return procedure

    def run(self, procedure, run_mode, image, drawables, config, run_data):
        layers = image.get_layers()
        layer = layers[0]
        Gimp.message(layer.get_name())
        
   
        layer_copy_drawable_proc = Gimp.get_pdb().lookup_procedure('gimp-layer-copy'); 
        layer_copy_drawable_config = layer_copy_drawable_proc.create_config(); 
        layer_copy_drawable_config.set_property('layer', layer); 
        layer_copy_result = layer_copy_drawable_proc.run(layer_copy_drawable_config); 
        success = layer_copy_result.index(0); 
        layer_copy = layer_copy_result.index(1)
        layer_copy.set_name(layer.get_name() + "_Copy")
        image.insert_layer(layer_copy, None, 0)
        Gimp.message("Copy")

  
        oilify_filter = Gimp.DrawableFilter.new(layer_copy, "gegl:oilify", "Oleo")
        oilify_config = oilify_filter.get_config()
        oilify_config.set_property('mask-radius', 8)
        oilify_config.set_property('exponent', 4)
        layer_copy.merge_filter(oilify_filter)

       
        second_layer_copy_drawable_proc = Gimp.get_pdb().lookup_procedure('gimp-layer-copy'); 
        second_layer_copy_drawable_config = second_layer_copy_drawable_proc.create_config(); 
        second_layer_copy_drawable_config.set_property('layer', layer_copy); 
        second_layer_copy_result = second_layer_copy_drawable_proc.run(second_layer_copy_drawable_config); 
        success = second_layer_copy_result.index(0); 
        second_layer_copy = second_layer_copy_result.index(1)
        second_layer_copy.set_name(layer.get_name() + "_Copy_2") 
        

        image.insert_layer(second_layer_copy, None, 0)
        Gimp.message("Second Copy")

        multiply_mode_proc = Gimp.get_pdb().lookup_procedure('gimp-layer-set-mode'); 
        multiply_mode_proc_config = multiply_mode_proc.create_config(); 
        multiply_mode_proc_config.set_property('layer', second_layer_copy); 
        multiply_mode_proc_config.set_property('mode', 3); 
        multiply_mode_result = multiply_mode_proc.run(multiply_mode_proc_config); 
        success = multiply_mode_result.index(0)
        Gimp.message("Multiply")

   
        third_layer_copy_drawable_proc = Gimp.get_pdb().lookup_procedure('gimp-layer-copy'); 
        third_layer_copy_drawable_config = third_layer_copy_drawable_proc.create_config(); 
        third_layer_copy_drawable_config.set_property('layer', layer); 
        third_layer_copy_result = third_layer_copy_drawable_proc.run(third_layer_copy_drawable_config); 
        success = third_layer_copy_result.index(0); 
        third_layer_copy = third_layer_copy_result.index(1)
        third_layer_copy.set_name(layer.get_name() + "_Copy_3") 
        image.insert_layer(third_layer_copy, None, 0)
        Gimp.message("Copy_3")

        grey_proc = Gimp.get_pdb().lookup_procedure('gimp-drawable-desaturate')
        grey_config = grey_proc.create_config()
        grey_config.set_property('drawable', third_layer_copy)
        grey_config.set_property('desaturate-mode', 0) 
        grey_proc.run(grey_config)
        Gimp.displays_flush()
        Gimp.message("Desaturate")

        third_layer_multiply_mode_proc = Gimp.get_pdb().lookup_procedure('gimp-layer-set-mode'); 
        third_layer_multiply_mode_config = third_layer_multiply_mode_proc.create_config(); 
        third_layer_multiply_mode_config.set_property('layer', third_layer_copy); 
        third_layer_multiply_mode_config.set_property('mode', 3); 
        third_layer_multiply_mode_result = third_layer_multiply_mode_proc.run(third_layer_multiply_mode_config); 
        success = third_layer_multiply_mode_result.index(0)
        Gimp.message("Multiply third layer")

        threshold_filter = Gimp.DrawableFilter.new(third_layer_copy, "gimp:threshold", "Umbral")
        threshold_filter_config = threshold_filter.get_config()
        threshold_filter_config.set_property('low', 0.5)
        threshold_filter_config.set_property('high', 1.0)
        third_layer_copy.append_filter(threshold_filter)
        
     
        third_layer_copy.append_filters()
        Gimp.message("threshold")

  
        Gimp.displays_flush()


        return procedure.new_return_values(Gimp.PDBStatusType.SUCCESS, GLib.Error())

if __name__ == '__main__':
    Gimp.main(MyFirstPlugin.__gtype__, sys.argv)