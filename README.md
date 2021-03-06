# LensKernelFFT
![lensKernels](http://www.nukepedia.com/images/users/bobroesler/LensKernelFFT_02.png)

LensKernelFFT is created by Bob Roesler, original and usage description can be found on nukepedia [here](http://www.nukepedia.com/gizmos/filter/lenskernelfft_v01/).
While working with it from time to time I've made some improvements to it, and decided to post it here.

## Improvements
* The kernels knobs on gizmo are now automatically filled by [`onUserCreate`](https://learn.foundry.com/nuke/developers/latest/pythondevguide/callbacks.html), which should be in the same directory as the [LensKernelFFT.gizmo](./LensKernelFFT.gizmo) file

* [localizeLensKernel](./localizeLensKernel.py) is an OnUserCreate function that executes when LensKernelFFT node is created.
    * If you created the node while working on a saved nuke script, it creates a "LensKernel" folder in your script directory and copy the  kernel files there, if they're not already there. After that, it relinks the kernel knobs to the kernel files in your script directory with relative paths. Making sure the kernel files are with the script and can be easily located.
    * If the nuke script is not saved, it will not copy the kernel files and the knobs are simply set to absolute paths.
* LensKernelFFT has a "pad frame" option that counter an "image wrap" issue with using FFT. It no longer works in later versions of nuke, this version fixes that by moving the reformat node in the gizmo. Quoting the "image wrap" issue from the nukepedia page.
    >One of the byproducts of FFT convolution is "image wrap", that is, the convolution of a pixel on the edge of the screen shows up on the opposite side. This is normally not an issue unless very bright pixels are at the edge of the image. The 'pad frame' parameter adds a number of pixels to each side of the image before the FFT tools are applied, and is meant to be a work around for that byproduct. The larger the '"pad frame" value, of course, the more time consuming the FFT conversion and convolution process.

## Setbacks
* For OnUserCreate to work I had to make LensKernelFFT into a gizmo instead of group, so you might have issue with render farm.
    * I am considering a future update that turn the gizmo node back into a group after the above.

## Installation
Simply download/clone this repository into your .nuke folder and add the line below to your init.py
```python
nuke.pluginAddPath('./LensKernelFFT')
```
