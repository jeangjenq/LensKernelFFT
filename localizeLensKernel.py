'''
Created by Jeang Jenq Loh on 24/10/2019
Created to work with LensKernelFFT gizmo
http://www.nukepedia.com/gizmos/filter/lenskernelfft_v01/finishdown?miv=1&mjv=1
Copies the kernel files to the script directory for easy access

Update 05/11/2019
Fixed file path issue and now convert to absolute path oncreate
'''

import nuke
import os
import shutil

current_dir = os.path.dirname(__file__) + '/'
kernels = ['35mmf14_normalized_v01.exr',
           '35mmf28_normalized_v01.exr',
           '35mmf56_normalized_v01.exr']
kernels_knobs = ['kernel14',
                 'kernel28',
                 'kernel56']

def localizeLensKernel():
    script_dir = os.path.dirname(nuke.Root().name())
    this = nuke.thisNode()
    if script_dir is not '':
        index = 0
        # Copy kernel files to script directory
        for kernel in kernels:
            old_file = current_dir + kernel
            new_dir = script_dir + '/LensKernel/'
            if not os.path.exists(new_dir):
                os.mkdir(new_dir)
            new_file = new_dir + kernel
            if not os.path.isfile(new_file):
                shutil.copy2(old_file, new_dir)

            # If kernel files are in script directory, set knob values accordingly
            if os.path.isfile(new_file):
                this[kernels_knobs[index]].setValue('[file dirname [value root.name]]/LensKernel/%s' % kernel)
                index += 1

        for node in nuke.allNodes(group=this):
            if node.Class() == 'Read':
                node['reload'].execute()
    else:
        index = 0
        for kernel in kernels:
            old_file = os.path.abspath(current_dir + kernel)
            this[kernels_knobs[index]].setValue(old_file)
            index += 1

nuke.addOnUserCreate(localizeLensKernel, nodeClass='LensKernelFFT')
