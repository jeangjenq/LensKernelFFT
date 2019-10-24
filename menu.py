import localizeLensKernel

toolbar = nuke.menu('Nodes').addMenu('ToolSets')
toolbar.addCommand('LensKernelFFT', 'nuke.tcl("LensKernelFFT")')