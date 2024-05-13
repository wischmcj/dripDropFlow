from __future__ import annotations

from src.canhydro.DataClasses import Flow

ten_cyls_cyls = [
    "Cylinder( cyl_id=0.0, x=[0.076822 0.076822], y=[-3.386935 -3.386935], z=[-0.595933 -0.5315  ], radius=0.222504, length=0.064433, branch_order=0.0, branch_id=0.0, volume=0.010021, parent_id=-1.0, reverse_branch_order=32.0, segment_id=0.0",
    "Cylinder( cyl_id=1.0, x=[0.076822 0.058561], y=[-3.386935 -3.328717], z=[-0.5315   -0.085599], radius=0.211908, length=0.450057, branch_order=0.0, branch_id=0.0, volume=0.063491, parent_id=0.0, reverse_branch_order=32.0, segment_id=0.0",
    "Cylinder( cyl_id=2.0, x=[0.058561 0.062703], y=[-3.328717 -3.334542], z=[-0.085599  0.232646], radius=0.197783, length=0.318325, branch_order=0.0, branch_id=0.0, volume=0.03912, parent_id=1.0, reverse_branch_order=32.0, segment_id=0.0",
    "Cylinder( cyl_id=3.0, x=[0.062703 0.06246 ], y=[-3.334542 -3.357087], z=[0.232646 0.499611], radius=0.198531, length=0.267916, branch_order=0.0, branch_id=0.0, volume=0.033174, parent_id=2.0, reverse_branch_order=32.0, segment_id=0.0",
    "Cylinder( cyl_id=4.0, x=[0.06246  0.073532], y=[-3.357087 -3.374155], z=[0.499611 0.779853], radius=0.188766, length=0.280979, branch_order=0.0, branch_id=0.0, volume=0.031454, parent_id=3.0, reverse_branch_order=32.0, segment_id=0.0",
    "Cylinder( cyl_id=5.0, x=[0.073532 0.067962], y=[-3.374155 -3.393301], z=[0.779853 1.05038 ], radius=0.187445, length=0.27126, branch_order=0.0, branch_id=0.0, volume=0.029942, parent_id=4.0, reverse_branch_order=32.0, segment_id=0.0",
    "Cylinder( cyl_id=6.0, x=[0.067962 0.062838], y=[-3.393301 -3.386649], z=[1.05038  1.311286], radius=0.19627, length=0.261041, branch_order=0.0, branch_id=0.0, volume=0.031591, parent_id=5.0, reverse_branch_order=32.0, segment_id=0.0",
    "Cylinder( cyl_id=7.0, x=[0.062838 0.055451], y=[-3.386649 -3.429066], z=[1.311286 1.581252], radius=0.182718, length=0.273378, branch_order=1.0, branch_id=0.0, volume=0.028673, parent_id=6.0, reverse_branch_order=32.0, segment_id=0.0",
    "Cylinder( cyl_id=8.0, x=[0.055451 0.073181], y=[-3.429066 -3.465325], z=[1.581252 1.802064], radius=0.203862, length=0.22447, branch_order=1.0, branch_id=0.0, volume=0.029308, parent_id=7.0, reverse_branch_order=32.0, segment_id=0.0",
    "Cylinder( cyl_id=9.0, x=[0.073181 0.062266], y=[-3.465325 -3.478196], z=[1.802064 2.056271], radius=0.196833, length=0.254767, branch_order=1.0, branch_id=0.0, volume=0.031009, parent_id=8.0, reverse_branch_order=31.0, segment_id=1.0",
]

ez_projection_cyls = [
    "Cylinder( cyl_id=0.0, x=[1. 4.], y=[1. 6.], z=[1. 7.], radius=1.0, length=0.064433, branch_order=0.0, branch_id=0.0, volume=0.010021, parent_id=-1.0, reverse_branch_order=32.0, segment_id=0.0",
    "Cylinder( cyl_id=1.0, x=[4. 7.], y=[ 6. 11.], z=[7. 1.], radius=1.0, length=0.064433, branch_order=0.0, branch_id=0.0, volume=0.010021, parent_id=0.0, reverse_branch_order=32.0, segment_id=0.0",
    "Cylinder( cyl_id=1.0, x=[ 7. 10.], y=[11. 16.], z=[ 1. -5.], radius=1.0, length=0.064433, branch_order=0.0, branch_id=0.0, volume=0.010021, parent_id=0.0, reverse_branch_order=32.0, segment_id=0.0",
    "Cylinder( cyl_id=1.0, x=[10.  7.], y=[16. 21.], z=[ -5. -11.], radius=1.0, length=0.064433, branch_order=0.0, branch_id=0.0, volume=0.010021, parent_id=0.0, reverse_branch_order=32.0, segment_id=0.0",
    "Cylinder( cyl_id=1.0, x=[ 7. 10.], y=[21. 16.], z=[-11. -17.], radius=1.0, length=0.064433, branch_order=0.0, branch_id=0.0, volume=0.010021, parent_id=0.0, reverse_branch_order=32.0, segment_id=0.0",
]

happy_path_cyls = [
    "Cylinder( cyl_id=0.0, x=[0.076822 0.076822], y=[-3.386935 -3.386935], z=[-0.595933 -0.5315  ], radius=0.222504, length=0.064433, branch_order=0.0, branch_id=0.0, volume=0.010021, parent_id=-1.0, reverse_branch_order=32.0, segment_id=0.0",
    "Cylinder( cyl_id=1.0, x=[0.076822 0.058561], y=[-3.386935 -3.328717], z=[-0.5315   -0.085599], radius=0.211908, length=0.450057, branch_order=0.0, branch_id=0.0, volume=0.063491, parent_id=0.0, reverse_branch_order=32.0, segment_id=0.0",
    "Cylinder( cyl_id=2.0, x=[0.058561 0.062703], y=[-3.328717 -3.334542], z=[-0.085599  0.232646], radius=0.197783, length=0.318325, branch_order=0.0, branch_id=0.0, volume=0.03912, parent_id=1.0, reverse_branch_order=32.0, segment_id=0.0",
    "Cylinder( cyl_id=3.0, x=[0.062703 0.06246 ], y=[-3.334542 -3.357087], z=[0.232646 0.499611], radius=0.198531, length=0.267916, branch_order=0.0, branch_id=0.0, volume=0.033174, parent_id=2.0, reverse_branch_order=32.0, segment_id=0.0",
    "Cylinder( cyl_id=4.0, x=[0.06246  0.073532], y=[-3.357087 -3.374155], z=[0.499611 0.779853], radius=0.188766, length=0.280979, branch_order=0.0, branch_id=0.0, volume=0.031454, parent_id=3.0, reverse_branch_order=32.0, segment_id=0.0",
    "Cylinder( cyl_id=5.0, x=[0.073532 0.067962], y=[-3.374155 -3.393301], z=[0.779853 1.05038 ], radius=0.187445, length=0.27126, branch_order=0.0, branch_id=0.0, volume=0.029942, parent_id=4.0, reverse_branch_order=32.0, segment_id=0.0",
    "Cylinder( cyl_id=6.0, x=[0.067962 0.062838], y=[-3.393301 -3.386649], z=[1.05038  1.311286], radius=0.19627, length=0.261041, branch_order=0.0, branch_id=0.0, volume=0.031591, parent_id=5.0, reverse_branch_order=32.0, segment_id=0.0",
    "Cylinder( cyl_id=7.0, x=[0.062838 0.055451], y=[-3.386649 -3.429066], z=[1.311286 1.581252], radius=0.182718, length=0.273378, branch_order=0.0, branch_id=0.0, volume=0.028673, parent_id=6.0, reverse_branch_order=32.0, segment_id=0.0",
    "Cylinder( cyl_id=8.0, x=[0.055451 0.073181], y=[-3.429066 -3.465325], z=[1.581252 1.802064], radius=0.203862, length=0.22447, branch_order=0.0, branch_id=0.0, volume=0.029308, parent_id=7.0, reverse_branch_order=32.0, segment_id=0.0",
    "Cylinder( cyl_id=9.0, x=[0.073181 0.062266], y=[-3.465325 -3.478196], z=[1.802064 2.056271], radius=0.196833, length=0.254767, branch_order=0.0, branch_id=0.0, volume=0.031009, parent_id=8.0, reverse_branch_order=31.0, segment_id=1.0",
    "Cylinder( cyl_id=10.0, x=[0.062266 0.027591], y=[-3.478196 -3.518976], z=[2.056271 2.315272], radius=0.20932, length=0.264475, branch_order=0.0, branch_id=0.0, volume=0.036404, parent_id=9.0, reverse_branch_order=30.0, segment_id=2.0",
    "Cylinder( cyl_id=11.0, x=[ 0.027591 -0.001305], y=[-3.518976 -3.560212], z=[2.315272 2.468256], radius=0.20932, length=0.161058, branch_order=0.0, branch_id=0.0, volume=0.022169, parent_id=10.0, reverse_branch_order=30.0, segment_id=2.0",
    "Cylinder( cyl_id=12.0, x=[-0.001305  0.034777], y=[-3.560212 -3.438469], z=[2.468256 2.858883], radius=0.124765, length=0.410746, branch_order=0.0, branch_id=0.0, volume=0.020087, parent_id=11.0, reverse_branch_order=29.0, segment_id=3.0",
    "Cylinder( cyl_id=13.0, x=[ 0.034777 -0.065825], y=[-3.438469 -3.331656], z=[2.858883 3.06936 ], radius=0.115601, length=0.256574, branch_order=0.0, branch_id=0.0, volume=0.010772, parent_id=12.0, reverse_branch_order=28.0, segment_id=4.0",
    "Cylinder( cyl_id=14.0, x=[-0.065825 -0.058826], y=[-3.331656 -3.424373], z=[3.06936  3.270241], radius=0.112207, length=0.221356, branch_order=0.0, branch_id=0.0, volume=0.008755, parent_id=13.0, reverse_branch_order=27.0, segment_id=5.0",
    "Cylinder( cyl_id=15.0, x=[-0.058826 -0.057322], y=[-3.424373 -3.428676], z=[3.270241 3.422008], radius=0.109626, length=0.151835, branch_order=0.0, branch_id=0.0, volume=0.005733, parent_id=14.0, reverse_branch_order=27.0, segment_id=5.0",
    "Cylinder( cyl_id=16.0, x=[-0.057322 -0.055536], y=[-3.428676 -3.418364], z=[3.422008 3.567363], radius=0.107314, length=0.145732, branch_order=0.0, branch_id=0.0, volume=0.005272, parent_id=15.0, reverse_branch_order=27.0, segment_id=5.0",
    "Cylinder( cyl_id=17.0, x=[-0.055536 -0.056154], y=[-3.418364 -3.416518], z=[3.567363 3.706142], radius=0.119733, length=0.138792, branch_order=0.0, branch_id=0.0, volume=0.006251, parent_id=16.0, reverse_branch_order=27.0, segment_id=5.0",
    "Cylinder( cyl_id=18.0, x=[-0.056154 -0.058504], y=[-3.416518 -3.401558], z=[3.706142 3.857456], radius=0.108127, length=0.15207, branch_order=0.0, branch_id=0.0, volume=0.005585, parent_id=17.0, reverse_branch_order=27.0, segment_id=5.0",
    "Cylinder( cyl_id=19.0, x=[-0.058504 -0.057836], y=[-3.401558 -3.297242], z=[3.857456 4.002476], radius=0.083356, length=0.178643, branch_order=0.0, branch_id=0.0, volume=0.0039, parent_id=18.0, reverse_branch_order=17.0, segment_id=6.0",
    "Cylinder( cyl_id=20.0, x=[-0.057836 -0.059261], y=[-3.297242 -3.271659], z=[4.002476 4.121282], radius=0.078515, length=0.121537, branch_order=0.0, branch_id=0.0, volume=0.002354, parent_id=19.0, reverse_branch_order=17.0, segment_id=6.0",
    "Cylinder( cyl_id=21.0, x=[-0.059261 -0.06571 ], y=[-3.271659 -3.257999], z=[4.121282 4.217405], radius=0.076817, length=0.097302, branch_order=0.0, branch_id=0.0, volume=0.001804, parent_id=20.0, reverse_branch_order=17.0, segment_id=6.0",
    "Cylinder( cyl_id=22.0, x=[-0.06571  -0.066685], y=[-3.257999 -3.235245], z=[4.217405 4.322664], radius=0.073089, length=0.107695, branch_order=0.0, branch_id=0.0, volume=0.001807, parent_id=21.0, reverse_branch_order=17.0, segment_id=6.0",
    "Cylinder( cyl_id=23.0, x=[-0.066685 -0.078122], y=[-3.235245 -3.222873], z=[4.322664 4.434789], radius=0.076579, length=0.113385, branch_order=0.0, branch_id=0.0, volume=0.002089, parent_id=22.0, reverse_branch_order=17.0, segment_id=6.0",
    "Cylinder( cyl_id=24.0, x=[-0.078122 -0.084576], y=[-3.222873 -3.199114], z=[4.434789 4.537954], radius=0.0772, length=0.106061, branch_order=0.0, branch_id=0.0, volume=0.001986, parent_id=23.0, reverse_branch_order=17.0, segment_id=6.0",
    "Cylinder( cyl_id=25.0, x=[-0.084576 -0.094275], y=[-3.199114 -3.192158], z=[4.537954 4.642884], radius=0.077654, length=0.105607, branch_order=0.0, branch_id=0.0, volume=0.002001, parent_id=24.0, reverse_branch_order=17.0, segment_id=6.0",
    "Cylinder( cyl_id=26.0, x=[-0.094275 -0.109448], y=[-3.192158 -3.177965], z=[4.642884 4.742207], radius=0.07615, length=0.101473, branch_order=0.0, branch_id=0.0, volume=0.001849, parent_id=25.0, reverse_branch_order=17.0, segment_id=6.0",
    "Cylinder( cyl_id=27.0, x=[-0.109448 -0.121389], y=[-3.177965 -3.17529 ], z=[4.742207 4.8489  ], radius=0.075838, length=0.107392, branch_order=0.0, branch_id=0.0, volume=0.00194, parent_id=26.0, reverse_branch_order=17.0, segment_id=6.0",
    "Cylinder( cyl_id=28.0, x=[-0.121389 -0.136877], y=[-3.17529  -3.164554], z=[4.8489   4.958056], radius=0.084646, length=0.110771, branch_order=0.0, branch_id=0.0, volume=0.002493, parent_id=27.0, reverse_branch_order=17.0, segment_id=6.0",
    "Cylinder( cyl_id=29.0, x=[-0.136877 -0.131187], y=[-3.164554 -3.141393], z=[4.958056 5.079266], radius=0.075341, length=0.123534, branch_order=0.0, branch_id=0.0, volume=0.002203, parent_id=28.0, reverse_branch_order=17.0, segment_id=6.0",
    "Cylinder( cyl_id=30.0, x=[-0.131187 -0.137226], y=[-3.141393 -3.123301], z=[5.079266 5.179019], radius=0.074351, length=0.10156, branch_order=0.0, branch_id=0.0, volume=0.001764, parent_id=29.0, reverse_branch_order=17.0, segment_id=6.0",
    "Cylinder( cyl_id=31.0, x=[-0.137226 -0.136859], y=[-3.123301 -3.10119 ], z=[5.179019 5.281189], radius=0.072841, length=0.104536, branch_order=0.0, branch_id=0.0, volume=0.001742, parent_id=30.0, reverse_branch_order=17.0, segment_id=6.0",
    "Cylinder( cyl_id=32.0, x=[-0.136859 -0.140386], y=[-3.10119  -3.087488], z=[5.281189 5.378628], radius=0.077031, length=0.098461, branch_order=0.0, branch_id=0.0, volume=0.001835, parent_id=31.0, reverse_branch_order=17.0, segment_id=6.0",
    "Cylinder( cyl_id=33.0, x=[-0.140386 -0.149544], y=[-3.087488 -3.072912], z=[5.378628 5.479159], radius=0.084333, length=0.101995, branch_order=0.0, branch_id=0.0, volume=0.002279, parent_id=32.0, reverse_branch_order=17.0, segment_id=6.0",
    "Cylinder( cyl_id=34.0, x=[-0.149544 -0.155951], y=[-3.072912 -3.064858], z=[5.479159 5.581015], radius=0.084304, length=0.102375, branch_order=0.0, branch_id=0.0, volume=0.002286, parent_id=33.0, reverse_branch_order=17.0, segment_id=6.0",
    "Cylinder( cyl_id=35.0, x=[-0.155951 -0.163805], y=[-3.064858 -3.049039], z=[5.581015 5.684423], radius=0.078626, length=0.104905, branch_order=0.0, branch_id=0.0, volume=0.002037, parent_id=34.0, reverse_branch_order=17.0, segment_id=6.0",
    "Cylinder( cyl_id=36.0, x=[-0.163805 -0.142775], y=[-3.049039 -3.034255], z=[5.684423 5.77434 ], radius=0.082411, length=0.09352, branch_order=0.0, branch_id=0.0, volume=0.001995, parent_id=35.0, reverse_branch_order=17.0, segment_id=6.0",
    "Cylinder( cyl_id=37.0, x=[-0.142775 -0.183385], y=[-3.034255 -3.040343], z=[5.77434  5.908583], radius=0.082411, length=0.140382, branch_order=0.0, branch_id=0.0, volume=0.002995, parent_id=36.0, reverse_branch_order=16.0, segment_id=7.0",
    "Cylinder( cyl_id=38.0, x=[-0.183385 -0.196242], y=[-3.040343 -3.022512], z=[5.908583 6.02986 ], radius=0.074488, length=0.123254, branch_order=0.0, branch_id=0.0, volume=0.002148, parent_id=37.0, reverse_branch_order=16.0, segment_id=7.0",
    "Cylinder( cyl_id=39.0, x=[-0.196242 -0.185009], y=[-3.022512 -3.005524], z=[6.02986  6.139235], radius=0.074488, length=0.111255, branch_order=0.0, branch_id=0.0, volume=0.001939, parent_id=38.0, reverse_branch_order=16.0, segment_id=7.0",
    "Cylinder( cyl_id=40.0, x=[-0.185009 -0.247645], y=[-3.005524 -3.027011], z=[6.139235 6.26064 ], radius=0.074304, length=0.13829, branch_order=0.0, branch_id=0.0, volume=0.002399, parent_id=39.0, reverse_branch_order=15.0, segment_id=8.0",
    "Cylinder( cyl_id=41.0, x=[-0.247645 -0.255977], y=[-3.027011 -3.020758], z=[6.26064  6.381853], radius=0.073989, length=0.121659, branch_order=0.0, branch_id=0.0, volume=0.002092, parent_id=40.0, reverse_branch_order=15.0, segment_id=8.0",
    "Cylinder( cyl_id=42.0, x=[-0.255977 -0.180642], y=[-3.020758 -2.98338 ], z=[6.381853 6.458277], radius=0.05174, length=0.113636, branch_order=0.0, branch_id=0.0, volume=0.000956, parent_id=41.0, reverse_branch_order=14.0, segment_id=9.0",
    "Cylinder( cyl_id=43.0, x=[-0.180642 -0.166534], y=[-2.98338  -2.947926], z=[6.458277 6.514814], radius=0.051677, length=0.068208, branch_order=0.0, branch_id=0.0, volume=0.000572, parent_id=42.0, reverse_branch_order=14.0, segment_id=9.0",
    "Cylinder( cyl_id=44.0, x=[-0.166534 -0.17596 ], y=[-2.947926 -2.948445], z=[6.514814 6.613315], radius=0.057275, length=0.098952, branch_order=0.0, branch_id=0.0, volume=0.00102, parent_id=43.0, reverse_branch_order=14.0, segment_id=9.0",
    "Cylinder( cyl_id=45.0, x=[-0.17596 -0.15214], y=[-2.948445 -2.909786], z=[6.613315 6.697043], radius=0.043887, length=0.095249, branch_order=0.0, branch_id=0.0, volume=0.000576, parent_id=44.0, reverse_branch_order=14.0, segment_id=9.0",
    "Cylinder( cyl_id=46.0, x=[-0.15214  -0.137455], y=[-2.909786 -2.893629], z=[6.697043 6.768243], radius=0.051571, length=0.074472, branch_order=0.0, branch_id=0.0, volume=0.000622, parent_id=45.0, reverse_branch_order=14.0, segment_id=9.0",
    "Cylinder( cyl_id=47.0, x=[-0.137455 -0.121855], y=[-2.893629 -2.87306 ], z=[6.768243 6.835912], radius=0.044826, length=0.072427, branch_order=0.0, branch_id=0.0, volume=0.000457, parent_id=46.0, reverse_branch_order=14.0, segment_id=9.0",
    "Cylinder( cyl_id=48.0, x=[-0.121855 -0.105806], y=[-2.87306  -2.850741], z=[6.835912 6.914823], radius=0.045028, length=0.083562, branch_order=0.0, branch_id=0.0, volume=0.000532, parent_id=47.0, reverse_branch_order=14.0, segment_id=9.0",
    "Cylinder( cyl_id=49.0, x=[-0.105806 -0.106141], y=[-2.850741 -2.826305], z=[6.914823 6.981695], radius=0.044382, length=0.071198, branch_order=0.0, branch_id=0.0, volume=0.000441, parent_id=48.0, reverse_branch_order=14.0, segment_id=9.0",
    "Cylinder( cyl_id=50.0, x=[-0.106141 -0.107509], y=[-2.826305 -2.805509], z=[6.981695 7.054587], radius=0.051491, length=0.075813, branch_order=0.0, branch_id=0.0, volume=0.000631, parent_id=49.0, reverse_branch_order=14.0, segment_id=9.0",
    "Cylinder( cyl_id=51.0, x=[-0.107509 -0.110174], y=[-2.805509 -2.787535], z=[7.054587 7.135171], radius=0.051472, length=0.082607, branch_order=0.0, branch_id=0.0, volume=0.000688, parent_id=50.0, reverse_branch_order=14.0, segment_id=9.0",
    "Cylinder( cyl_id=52.0, x=[-0.110174 -0.102546], y=[-2.787535 -2.768837], z=[7.135171 7.207126], radius=0.046712, length=0.074735, branch_order=0.0, branch_id=0.0, volume=0.000512, parent_id=51.0, reverse_branch_order=14.0, segment_id=9.0",
    "Cylinder( cyl_id=53.0, x=[-0.102546 -0.098577], y=[-2.768837 -2.739703], z=[7.207126 7.284497], radius=0.051431, length=0.08277, branch_order=0.0, branch_id=0.0, volume=0.000688, parent_id=52.0, reverse_branch_order=14.0, segment_id=9.0",
    "Cylinder( cyl_id=54.0, x=[-0.098577 -0.081751], y=[-2.739703 -2.720897], z=[7.284497 7.355692], radius=0.044846, length=0.075535, branch_order=0.0, branch_id=0.0, volume=0.000477, parent_id=53.0, reverse_branch_order=14.0, segment_id=9.0",
    "Cylinder( cyl_id=55.0, x=[-0.081751 -0.083484], y=[-2.720897 -2.701513], z=[7.355692 7.432121], radius=0.051389, length=0.078868, branch_order=0.0, branch_id=0.0, volume=0.000654, parent_id=54.0, reverse_branch_order=14.0, segment_id=9.0",
    "Cylinder( cyl_id=56.0, x=[-0.083484 -0.07584 ], y=[-2.701513 -2.686353], z=[7.432121 7.497618], radius=0.051372, length=0.067662, branch_order=0.0, branch_id=0.0, volume=0.000561, parent_id=55.0, reverse_branch_order=14.0, segment_id=9.0",
    "Cylinder( cyl_id=57.0, x=[-0.07584  -0.059804], y=[-2.686353 -2.671483], z=[7.497618 7.557284], radius=0.05215, length=0.063547, branch_order=0.0, branch_id=0.0, volume=0.000543, parent_id=56.0, reverse_branch_order=14.0, segment_id=9.0",
    "Cylinder( cyl_id=58.0, x=[-0.059804 -0.04742 ], y=[-2.671483 -2.643733], z=[7.557284 7.617007], radius=0.051333, length=0.06701, branch_order=0.0, branch_id=0.0, volume=0.000555, parent_id=57.0, reverse_branch_order=14.0, segment_id=9.0",
    "Cylinder( cyl_id=59.0, x=[-0.04742  -0.056788], y=[-2.643733 -2.617914], z=[7.617007 7.723978], radius=0.047613, length=0.110441, branch_order=0.0, branch_id=0.0, volume=0.000787, parent_id=58.0, reverse_branch_order=13.0, segment_id=10.0",
    "Cylinder( cyl_id=60.0, x=[-0.056788 -0.090898], y=[-2.617914 -2.551916], z=[7.723978 7.775558], radius=0.040756, length=0.090442, branch_order=0.0, branch_id=0.0, volume=0.000472, parent_id=59.0, reverse_branch_order=11.0, segment_id=11.0",
    "Cylinder( cyl_id=61.0, x=[-0.090898 -0.106074], y=[-2.551916 -2.50664 ], z=[7.775558 7.830104], radius=0.038178, length=0.072495, branch_order=0.0, branch_id=0.0, volume=0.000332, parent_id=60.0, reverse_branch_order=11.0, segment_id=11.0",
    "Cylinder( cyl_id=62.0, x=[-0.106074 -0.122123], y=[-2.50664  -2.471698], z=[7.830104 7.885584], radius=0.038446, length=0.067503, branch_order=0.0, branch_id=0.0, volume=0.000313, parent_id=61.0, reverse_branch_order=11.0, segment_id=11.0",
    "Cylinder( cyl_id=63.0, x=[-0.122123 -0.14285 ], y=[-2.471698 -2.427033], z=[7.885584 7.934678], radius=0.037605, length=0.069532, branch_order=0.0, branch_id=0.0, volume=0.000309, parent_id=62.0, reverse_branch_order=11.0, segment_id=11.0",
    "Cylinder( cyl_id=64.0, x=[-0.14285  -0.157797], y=[-2.427033 -2.393002], z=[7.934678 7.993905], radius=0.038695, length=0.069924, branch_order=0.0, branch_id=0.0, volume=0.000329, parent_id=63.0, reverse_branch_order=11.0, segment_id=11.0",
    "Cylinder( cyl_id=65.0, x=[-0.157797 -0.168682], y=[-2.393002 -2.381461], z=[7.993905 8.042353], radius=0.038695, length=0.050979, branch_order=0.0, branch_id=0.0, volume=0.00024, parent_id=64.0, reverse_branch_order=11.0, segment_id=11.0",
    "Cylinder( cyl_id=66.0, x=[-0.168682 -0.198118], y=[-2.381461 -2.316807], z=[8.042353 8.10925 ], radius=0.036929, length=0.097579, branch_order=0.0, branch_id=0.0, volume=0.000418, parent_id=65.0, reverse_branch_order=10.0, segment_id=12.0",
    "Cylinder( cyl_id=67.0, x=[-0.198118 -0.216827], y=[-2.316807 -2.290872], z=[8.10925  8.168945], radius=0.035127, length=0.067721, branch_order=0.0, branch_id=0.0, volume=0.000263, parent_id=66.0, reverse_branch_order=10.0, segment_id=12.0",
    "Cylinder( cyl_id=68.0, x=[-0.216827 -0.234318], y=[-2.290872 -2.259834], z=[8.168945 8.232016], radius=0.036007, length=0.072439, branch_order=0.0, branch_id=0.0, volume=0.000295, parent_id=67.0, reverse_branch_order=10.0, segment_id=12.0",
    "Cylinder( cyl_id=69.0, x=[-0.234318 -0.249533], y=[-2.259834 -2.230372], z=[8.232016 8.288784], radius=0.036566, length=0.065742, branch_order=0.0, branch_id=0.0, volume=0.000276, parent_id=68.0, reverse_branch_order=10.0, segment_id=12.0",
    "Cylinder( cyl_id=70.0, x=[-0.249533 -0.268207], y=[-2.230372 -2.2044  ], z=[8.288784 8.352136], radius=0.036996, length=0.070971, branch_order=0.0, branch_id=0.0, volume=0.000305, parent_id=69.0, reverse_branch_order=10.0, segment_id=12.0",
    "Cylinder( cyl_id=71.0, x=[-0.268207 -0.286132], y=[-2.2044   -2.176682], z=[8.352136 8.403738], radius=0.035783, length=0.061256, branch_order=0.0, branch_id=0.0, volume=0.000246, parent_id=70.0, reverse_branch_order=10.0, segment_id=12.0",
    "Cylinder( cyl_id=72.0, x=[-0.286132 -0.303921], y=[-2.176682 -2.142636], z=[8.403738 8.473344], radius=0.036562, length=0.079502, branch_order=0.0, branch_id=0.0, volume=0.000334, parent_id=71.0, reverse_branch_order=10.0, segment_id=12.0",
    "Cylinder( cyl_id=73.0, x=[-0.303921 -0.315822], y=[-2.142636 -2.117104], z=[8.473344 8.539532], radius=0.042866, length=0.071933, branch_order=0.0, branch_id=0.0, volume=0.000415, parent_id=72.0, reverse_branch_order=10.0, segment_id=12.0",
    "Cylinder( cyl_id=74.0, x=[-0.315822 -0.335579], y=[-2.117104 -2.071696], z=[8.539532 8.600119], radius=0.037867, length=0.07825, branch_order=0.0, branch_id=0.0, volume=0.000352, parent_id=73.0, reverse_branch_order=10.0, segment_id=12.0",
    "Cylinder( cyl_id=75.0, x=[-0.335579 -0.347286], y=[-2.071696 -2.045686], z=[8.600119 8.666266], radius=0.039886, length=0.072034, branch_order=0.0, branch_id=0.0, volume=0.00036, parent_id=74.0, reverse_branch_order=10.0, segment_id=12.0",
    "Cylinder( cyl_id=76.0, x=[-0.347286 -0.363641], y=[-2.045686 -2.024581], z=[8.666266 8.731817], radius=0.044711, length=0.07078, branch_order=0.0, branch_id=0.0, volume=0.000445, parent_id=75.0, reverse_branch_order=10.0, segment_id=12.0",
    "Cylinder( cyl_id=77.0, x=[-0.363641 -0.367266], y=[-2.024581 -1.956941], z=[8.731817 8.793305], radius=0.03301, length=0.091483, branch_order=0.0, branch_id=0.0, volume=0.000313, parent_id=76.0, reverse_branch_order=9.0, segment_id=13.0",
    "Cylinder( cyl_id=78.0, x=[-0.367266 -0.368869], y=[-1.956941 -1.924685], z=[8.793305 8.837513], radius=0.032015, length=0.054749, branch_order=0.0, branch_id=0.0, volume=0.000176, parent_id=77.0, reverse_branch_order=9.0, segment_id=13.0",
    "Cylinder( cyl_id=79.0, x=[-0.368869 -0.374497], y=[-1.924685 -1.884855], z=[8.837513 8.885968], radius=0.03024, length=0.062976, branch_order=0.0, branch_id=0.0, volume=0.000181, parent_id=78.0, reverse_branch_order=9.0, segment_id=13.0",
    "Cylinder( cyl_id=80.0, x=[-0.374497 -0.376017], y=[-1.884855 -1.84986 ], z=[8.885968 8.937917], radius=0.028642, length=0.062655, branch_order=0.0, branch_id=0.0, volume=0.000161, parent_id=79.0, reverse_branch_order=9.0, segment_id=13.0",
    "Cylinder( cyl_id=81.0, x=[-0.376017 -0.382543], y=[-1.84986  -1.822089], z=[8.937917 8.988857], radius=0.034786, length=0.058383, branch_order=0.0, branch_id=0.0, volume=0.000222, parent_id=80.0, reverse_branch_order=9.0, segment_id=13.0",
    "Cylinder( cyl_id=82.0, x=[-0.382543 -0.38097 ], y=[-1.822089 -1.788348], z=[8.988857 9.050148], radius=0.032496, length=0.069983, branch_order=0.0, branch_id=0.0, volume=0.000232, parent_id=81.0, reverse_branch_order=9.0, segment_id=13.0",
    "Cylinder( cyl_id=83.0, x=[-0.38097  -0.404069], y=[-1.788348 -1.738043], z=[9.050148 9.096119], radius=0.030276, length=0.071954, branch_order=0.0, branch_id=0.0, volume=0.000207, parent_id=82.0, reverse_branch_order=9.0, segment_id=13.0",
    "Cylinder( cyl_id=84.0, x=[-0.404069 -0.419862], y=[-1.738043 -1.720933], z=[9.096119 9.157446], radius=0.029328, length=0.065598, branch_order=0.0, branch_id=0.0, volume=0.000177, parent_id=83.0, reverse_branch_order=9.0, segment_id=13.0",
    "Cylinder( cyl_id=85.0, x=[-0.419862 -0.42789 ], y=[-1.720933 -1.685086], z=[9.157446 9.214547], radius=0.033145, length=0.067897, branch_order=0.0, branch_id=0.0, volume=0.000234, parent_id=84.0, reverse_branch_order=9.0, segment_id=13.0",
    "Cylinder( cyl_id=86.0, x=[-0.42789  -0.446164], y=[-1.685086 -1.649179], z=[9.214547 9.25704 ], radius=0.036584, length=0.058557, branch_order=0.0, branch_id=0.0, volume=0.000246, parent_id=85.0, reverse_branch_order=9.0, segment_id=13.0",
    "Cylinder( cyl_id=87.0, x=[-0.446164 -0.462466], y=[-1.649179 -1.588237], z=[9.25704  9.302596], radius=0.031391, length=0.077814, branch_order=0.0, branch_id=0.0, volume=0.000241, parent_id=86.0, reverse_branch_order=9.0, segment_id=13.0",
    "Cylinder( cyl_id=88.0, x=[-0.462466 -0.4719  ], y=[-1.588237 -1.552052], z=[9.302596 9.340372], radius=0.037065, length=0.053154, branch_order=0.0, branch_id=0.0, volume=0.000229, parent_id=87.0, reverse_branch_order=9.0, segment_id=13.0",
    "Cylinder( cyl_id=89.0, x=[-0.4719   -0.511085], y=[-1.552052 -1.491902], z=[9.340372 9.389201], radius=0.032378, length=0.08682, branch_order=0.0, branch_id=0.0, volume=0.000286, parent_id=88.0, reverse_branch_order=9.0, segment_id=13.0",
    "Cylinder( cyl_id=90.0, x=[-0.511085 -0.508096], y=[-1.491902 -1.473524], z=[9.389201 9.448287], radius=0.032622, length=0.06195, branch_order=0.0, branch_id=0.0, volume=0.000207, parent_id=89.0, reverse_branch_order=8.0, segment_id=14.0",
    "Cylinder( cyl_id=91.0, x=[-0.508096 -0.489413], y=[-1.473524 -1.45054 ], z=[9.448287 9.508954], radius=0.028499, length=0.067511, branch_order=0.0, branch_id=0.0, volume=0.000172, parent_id=90.0, reverse_branch_order=8.0, segment_id=14.0",
    "Cylinder( cyl_id=92.0, x=[-0.489413 -0.496181], y=[-1.45054  -1.422676], z=[9.508954 9.569169], radius=0.027423, length=0.066694, branch_order=0.0, branch_id=0.0, volume=0.000158, parent_id=91.0, reverse_branch_order=8.0, segment_id=14.0",
    "Cylinder( cyl_id=93.0, x=[-0.496181 -0.499306], y=[-1.422676 -1.402556], z=[9.569169 9.61718 ], radius=0.032231, length=0.05215, branch_order=0.0, branch_id=0.0, volume=0.00017, parent_id=92.0, reverse_branch_order=8.0, segment_id=14.0",
    "Cylinder( cyl_id=94.0, x=[-0.499306 -0.501735], y=[-1.402556 -1.383654], z=[9.61718  9.681935], radius=0.029584, length=0.067501, branch_order=0.0, branch_id=0.0, volume=0.000186, parent_id=93.0, reverse_branch_order=8.0, segment_id=14.0",
    "Cylinder( cyl_id=95.0, x=[-0.501735 -0.485299], y=[-1.383654 -1.349411], z=[9.681935 9.737485], radius=0.032202, length=0.067294, branch_order=0.0, branch_id=0.0, volume=0.000219, parent_id=94.0, reverse_branch_order=8.0, segment_id=14.0",
    "Cylinder( cyl_id=96.0, x=[-0.485299 -0.473887], y=[-1.349411 -1.292763], z=[9.737485 9.808151], radius=0.032156, length=0.091286, branch_order=0.0, branch_id=0.0, volume=0.000297, parent_id=95.0, reverse_branch_order=8.0, segment_id=14.0",
    "Cylinder( cyl_id=97.0, x=[-0.473887 -0.509462], y=[-1.292763 -1.247464], z=[9.808151 9.88034 ], radius=0.031997, length=0.092352, branch_order=0.0, branch_id=0.0, volume=0.000297, parent_id=96.0, reverse_branch_order=8.0, segment_id=14.0",
    "Cylinder( cyl_id=98.0, x=[-0.509462 -0.46907 ], y=[-1.247464 -1.110556], z=[9.88034  9.935555], radius=0.026386, length=0.153049, branch_order=0.0, branch_id=0.0, volume=0.000335, parent_id=97.0, reverse_branch_order=7.0, segment_id=15.0",
    "Cylinder( cyl_id=99.0, x=[-0.46907  -0.494318], y=[-1.110556 -1.038573], z=[ 9.935555 10.002307], radius=0.026233, length=0.101364, branch_order=0.0, branch_id=0.0, volume=0.000219, parent_id=98.0, reverse_branch_order=7.0, segment_id=15.0",
    "Cylinder( cyl_id=100.0, x=[-0.494318 -0.501549], y=[-1.038573 -1.036312], z=[10.002307 10.092412], radius=0.024533, length=0.090423, branch_order=0.0, branch_id=0.0, volume=0.000171, parent_id=99.0, reverse_branch_order=6.0, segment_id=16.0",
    "Cylinder( cyl_id=101.0, x=[-0.501549 -0.440411], y=[-1.036312 -1.053649], z=[10.092412 10.163284], radius=0.019178, length=0.095191, branch_order=0.0, branch_id=0.0, volume=0.00011, parent_id=100.0, reverse_branch_order=5.0, segment_id=17.0",
    "Cylinder( cyl_id=102.0, x=[-0.440411 -0.437682], y=[-1.053649 -1.029842], z=[10.163284 10.217745], radius=0.019129, length=0.0595, branch_order=0.0, branch_id=0.0, volume=6.8e-05, parent_id=101.0, reverse_branch_order=5.0, segment_id=17.0",
    "Cylinder( cyl_id=103.0, x=[-0.437682 -0.423197], y=[-1.029842 -1.00204 ], z=[10.217745 10.27936 ], radius=0.019104, length=0.069132, branch_order=0.0, branch_id=0.0, volume=7.9e-05, parent_id=102.0, reverse_branch_order=5.0, segment_id=17.0",
    "Cylinder( cyl_id=104.0, x=[-0.423197 -0.383383], y=[-1.00204  -0.969435], z=[10.27936  10.339124], radius=0.01905, length=0.078867, branch_order=0.0, branch_id=0.0, volume=9e-05, parent_id=103.0, reverse_branch_order=5.0, segment_id=17.0",
    "Cylinder( cyl_id=105.0, x=[-0.383383 -0.363553], y=[-0.969435 -1.01903 ], z=[10.339124 10.495052], radius=0.018641, length=0.164822, branch_order=0.0, branch_id=0.0, volume=0.00018, parent_id=104.0, reverse_branch_order=4.0, segment_id=18.0",
    "Cylinder( cyl_id=106.0, x=[-0.363553 -0.332222], y=[-1.01903  -1.151523], z=[10.495052 10.622299], radius=0.017021, length=0.186353, branch_order=0.0, branch_id=0.0, volume=0.00017, parent_id=105.0, reverse_branch_order=3.0, segment_id=19.0",
    "Cylinder( cyl_id=138.0, x=[-0.383383 -0.376465], y=[-0.969435 -0.878738], z=[10.339124 10.340219], radius=0.004507, length=0.090968, branch_order=1.0, branch_id=4.0, volume=6e-06, parent_id=104.0, reverse_branch_order=2.0, segment_id=28.0",
    "Cylinder( cyl_id=139.0, x=[-0.376465 -0.421839], y=[-0.878738 -0.783571], z=[10.340219 10.350996], radius=0.004334, length=0.105979, branch_order=1.0, branch_id=4.0, volume=6e-06, parent_id=138.0, reverse_branch_order=2.0, segment_id=28.0",
    "Cylinder( cyl_id=140.0, x=[-0.421839 -0.342949], y=[-0.783571 -0.749089], z=[10.350996 10.412333], radius=0.004115, length=0.105711, branch_order=1.0, branch_id=4.0, volume=6e-06, parent_id=139.0, reverse_branch_order=2.0, segment_id=28.0",
    "Cylinder( cyl_id=141.0, x=[-0.342949 -0.279745], y=[-0.749089 -0.658196], z=[10.412333 10.448264], radius=0.003875, length=0.116393, branch_order=1.0, branch_id=4.0, volume=5e-06, parent_id=140.0, reverse_branch_order=2.0, segment_id=28.0",
    "Cylinder( cyl_id=142.0, x=[-0.279745 -0.246297], y=[-0.658196 -0.599935], z=[10.448264 10.49903 ], radius=0.003577, length=0.084204, branch_order=1.0, branch_id=4.0, volume=3e-06, parent_id=141.0, reverse_branch_order=2.0, segment_id=28.0",
    "Cylinder( cyl_id=143.0, x=[-0.246297 -0.199178], y=[-0.599935 -0.539375], z=[10.49903  10.507596], radius=0.00333, length=0.077208, branch_order=1.0, branch_id=4.0, volume=3e-06, parent_id=142.0, reverse_branch_order=2.0, segment_id=28.0",
    "Cylinder( cyl_id=144.0, x=[-0.199178 -0.123813], y=[-0.539375 -0.497206], z=[10.507596 10.572537], radius=0.002566, length=0.108053, branch_order=1.0, branch_id=4.0, volume=2e-06, parent_id=143.0, reverse_branch_order=1.0, segment_id=29.0",
    "Cylinder( cyl_id=145.0, x=[-0.123813 -0.051498], y=[-0.497206 -0.454615], z=[10.572537 10.598556], radius=0.0025, length=0.087866, branch_order=1.0, branch_id=4.0, volume=2e-06, parent_id=144.0, reverse_branch_order=1.0, segment_id=29.0",
    "Cylinder( cyl_id=146.0, x=[-0.051498  0.052574], y=[-0.454615 -0.451659], z=[10.598556 10.618096], radius=0.0025, length=0.105932, branch_order=1.0, branch_id=4.0, volume=2e-06, parent_id=145.0, reverse_branch_order=1.0, segment_id=29.0",
    "Cylinder( cyl_id=147.0, x=[0.052574 0.07618 ], y=[-0.451659 -0.383481], z=[10.618096 10.653787], radius=0.0025, length=0.080494, branch_order=1.0, branch_id=4.0, volume=2e-06, parent_id=146.0, reverse_branch_order=1.0, segment_id=29.0",
    "Cylinder( cyl_id=148.0, x=[-0.437682 -0.387682], y=[-1.029842 -0.979842], z=[10.217745 10.117745], radius=0.004507, length=0.090968, branch_order=1.0, branch_id=4.0, volume=6e-06, parent_id=102.0, reverse_branch_order=2.0, segment_id=28.0",
    "Cylinder( cyl_id=149.0, x=[-0.387682 -0.337682], y=[-0.979842 -0.929842], z=[10.117745 10.017745], radius=0.004334, length=0.105979, branch_order=1.0, branch_id=4.0, volume=6e-06, parent_id=148.0, reverse_branch_order=2.0, segment_id=28.0",
    "Cylinder( cyl_id=150.0, x=[-0.337682 -0.287682], y=[-0.929842 -0.879842], z=[10.017745  9.917745], radius=0.004115, length=0.105711, branch_order=1.0, branch_id=4.0, volume=6e-06, parent_id=149.0, reverse_branch_order=2.0, segment_id=28.0",
]

ez_projection_xy = [0.7996, -0.7996, -0.7996, -0.7996, -0.7996]
ez_projection_xz = [0.6405, 0.6405, 0.6405, 0.6405, -0.6405]
ez_projection_yz = [0.3667, 0.3667, 0.3667, -0.3667, 0.3667]

ten_cyls_id_one = [1.0]
ten_cyls_bo_one = [7.0, 8.0, 9.0]
ten_cyls_bo_and_len = [0.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 8.0]

ten_cyls_is_stem = (True, True, True, True, True, True, True, True, True, True)

happy_path_is_stem = (
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    False,
    False,
    False,
)

small_tree_is_stem = (
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    False,
    False,
    False,
    False,
    False,
    False,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    False,
    False,
    False,
    True,
    True,
    False,
    False,
    False,
    False,
    False,
    True,
    True,
    False,
    False,
    False,
    False,
    True,
    True,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    True,
    True,
    True,
    False,
    True,
    True,
    True,
    True,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    False,
    False,
    False,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    False,
    False,
    True,
    True,
    False,
    False,
    False,
    False,
    False,
    True,
    True,
    True,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    True,
    True,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    True,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    True,
    True,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
)
drip_mid_stem_map = (
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
)

drip_adj_stem_map = (
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
)

drip_on_trunk_stem_map = (
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    True,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
    False,
)

ten_cyls_rows_proj_XZ = []
ten_cyls_rows_proj_XY = []
ten_cyls_rows_proj_YZ = []

ten_cyls_flows = [
    Flow(
        num_cylinders=10,
        projected_area=1.332563385222201,
        surface_area=3.3102009951007805,
        angle_sum=13.311017528987755,
        volume=0.327783,
        sa_to_vol=100.98563451833446,
        drip_node_id=0,
        drip_node_loc=(0.076822, -3.386935),
    )
]

happy_path_flows = [
    Flow(
        num_cylinders=117,
        projected_area=2.966550840828153,
        surface_area=7.4149259812596755,
        angle_sum=127.43768060688681,
        volume=0.5217939999999999,
        sa_to_vol=10791.467322627153,
        drip_node_id=0,
        drip_node_loc=(0.076822, -3.386935),
    ),
    Flow(
        num_cylinders=2,
        projected_area=0.0013505874589177964,
        surface_area=0.005462009191244954,
        angle_sum=-1.9106332362490235,
        volume=1.2e-05,
        sa_to_vol=910.3348652074924,
        drip_node_id=150,
        drip_node_loc=(-0.337682, -0.929842, 10.017745),
    ),
]

small_tree_flows =  [
Flow(num_cylinders=216
     ,projected_area=16.517060215326925
     ,surface_area=19.49507498855058
     ,angle_sum=180.03288665020412
     ,volume=3.9062959999999998
     ,sa_to_vol=83646.49652248439
     ,drip_node_id=0
     ,drip_node_loc=(-0.299115
     ,2.537844))
     ,
Flow(num_cylinders=2
     ,projected_area=0.0005597565466076131
     ,surface_area=0.001924052712727801
     ,angle_sum=-0.8861661864942612
     ,volume=2e-06
     ,sa_to_vol=1924.052712727801
     ,drip_node_id=148
     ,drip_node_loc=(1.704854
     ,2.706883
     ,14.222385))
     ,
Flow(num_cylinders=4
     ,projected_area=0.0012679984136685896
     ,surface_area=0.0043875954238933096
     ,angle_sum=-1.1103646559240672
     ,volume=4.9999999999999996e-06
     ,sa_to_vol=3681.4517891642977
     ,drip_node_id=150
     ,drip_node_loc=(1.563945
     ,2.768174
     ,14.254736))
     ,
Flow(num_cylinders=1
     ,projected_area=0.00026175097799692134
     ,surface_area=0.0008268043545717619
     ,angle_sum=0.20259148846207123
     ,volume=1e-06
     ,sa_to_vol=826.8043545717619
     ,drip_node_id=159
     ,drip_node_loc=(1.351427
     ,2.473622
     ,14.399221))
     ,
Flow(num_cylinders=3
     ,projected_area=0.0008824774277666259
     ,surface_area=0.0032463019367339413
     ,angle_sum=-1.7087376025874943
     ,volume=3e-06
     ,sa_to_vol=3246.3019367339416
     ,drip_node_id=164
     ,drip_node_loc=(1.097889
     ,2.391842
     ,14.289977))
     ,
Flow(num_cylinders=2
     ,projected_area=0.0006600186476422296
     ,surface_area=0.0023746199311056493
     ,angle_sum=0.534393748750537
     ,volume=3e-06
     ,sa_to_vol=1719.5271769974715
     ,drip_node_id=175
     ,drip_node_loc=(1.709415
     ,2.355251
     ,14.614428))
     ,
Flow(num_cylinders=2
     ,projected_area=0.0004876054032408554
     ,surface_area=0.001917581031861406
     ,angle_sum=1.1425108485836808
     ,volume=3e-06
     ,sa_to_vol=1179.8879529087187
     ,drip_node_id=179
     ,drip_node_loc=(1.70026
     ,2.315748
     ,14.500385))
     ,
Flow(num_cylinders=1
     ,projected_area=0.00041651108754572896
     ,surface_area=0.0014212408085207547
     ,angle_sum=-0.4465420656788475
     ,volume=2e-06
     ,sa_to_vol=710.6204042603774
     ,drip_node_id=183
     ,drip_node_loc=(1.496279
     ,2.240669
     ,14.513242))
     ,
Flow(num_cylinders=2
     ,projected_area=0.0012733736410329834
     ,surface_area=0.004064592575214475
     ,angle_sum=-0.3665923044681696
     ,volume=4.9999999999999996e-06
     ,sa_to_vol=1666.127955868079
     ,drip_node_id=187
     ,drip_node_loc=(1.856726
     ,2.421858
     ,14.290216))
     ,
Flow(num_cylinders=0
     ,projected_area=0.0
     ,surface_area=0.0
     ,angle_sum=0.0
     ,volume=0.0
     ,sa_to_vol=0.0
     ,drip_node_id=189
     ,drip_node_loc=(1.996825
     ,2.461936
     ,14.202651))
     ,
Flow(num_cylinders=6
     ,projected_area=0.0022330283517565724
     ,surface_area=0.007333246943678708
     ,angle_sum=2.127804515876493
     ,volume=9.999999999999999e-06
     ,sa_to_vol=4446.06831715825
     ,drip_node_id=193
     ,drip_node_loc=(1.643961
     ,2.511586
     ,13.986929))
     ,
Flow(num_cylinders=1
     ,projected_area=0.00020343043979622444
     ,surface_area=0.0006478435290600194
     ,angle_sum=0.2846026246124941
     ,volume=1e-06
     ,sa_to_vol=647.8435290600194
     ,drip_node_id=198
     ,drip_node_loc=(1.351915
     ,2.628367
     ,14.041021))
     ,
Flow(num_cylinders=3
     ,projected_area=0.0007860084747630203
     ,surface_area=0.003617512524682111
     ,angle_sum=-2.5833501908977685
     ,volume=4.9999999999999996e-06
     ,sa_to_vol=2085.8447343876755
     ,drip_node_id=208
     ,drip_node_loc=(1.38855
     ,2.815
     ,14.07765))
     ,
Flow(num_cylinders=2
     ,projected_area=0.0006471769977986668
     ,surface_area=0.0020395847825635657
     ,angle_sum=0.26090730746353386
     ,volume=2e-06
     ,sa_to_vol=2039.584782563566
     ,drip_node_id=209
     ,drip_node_loc=(1.342538
     ,2.756578
     ,14.240517))
     ,
Flow(num_cylinders=8
     ,projected_area=0.0017034251569991014
     ,surface_area=0.007463890074178239
     ,angle_sum=5.354426428330182
     ,volume=8.999999999999999e-06
     ,sa_to_vol=6831.314685414667
     ,drip_node_id=214
     ,drip_node_loc=(1.245285
     ,2.627565
     ,14.031447))
     ,
Flow(num_cylinders=3
     ,projected_area=0.0012809041391582444
     ,surface_area=0.004173213141212342
     ,angle_sum=0.3207042500076585
     ,volume=6e-06
     ,sa_to_vol=2086.606570606171
     ,drip_node_id=219
     ,drip_node_loc=(1.116967
     ,2.759733
     ,13.987866))
     ,
Flow(num_cylinders=2
     ,projected_area=0.0008570559793830896
     ,surface_area=0.0027383692365015432
     ,angle_sum=-0.10344238545184348
     ,volume=4e-06
     ,sa_to_vol=1369.1846182507718
     ,drip_node_id=222
     ,drip_node_loc=(1.643961
     ,2.511586
     ,13.986929))
     ,
Flow(num_cylinders=0
     ,projected_area=0.0
     ,surface_area=0.0
     ,angle_sum=0.0
     ,volume=0.0
     ,sa_to_vol=0.0
     ,drip_node_id=227
     ,drip_node_loc=(1.844739
     ,2.507194
     ,13.979754))
     ,
Flow(num_cylinders=18
     ,projected_area=0.005313162793692856
     ,surface_area=0.021339283807471944
     ,angle_sum=10.274852917465788
     ,volume=2.6e-05
     ,sa_to_vol=14370.354273860652
     ,drip_node_id=232
     ,drip_node_loc=(1.858071
     ,2.197374
     ,13.956121))
     ,
Flow(num_cylinders=7
     ,projected_area=0.0029795345832851253
     ,surface_area=0.013586461456943049
     ,angle_sum=4.695171005225782
     ,volume=1.8e-05
     ,sa_to_vol=5378.31106616918
     ,drip_node_id=242
     ,drip_node_loc=(2.033054
     ,1.966092
     ,14.337358))
     ,
Flow(num_cylinders=0
     ,projected_area=0.0
     ,surface_area=0.0
     ,angle_sum=0.0
     ,volume=0.0
     ,sa_to_vol=0.0
     ,drip_node_id=247
     ,drip_node_loc=(2.094222
     ,2.008671
     ,14.558278))
     ,
Flow(num_cylinders=1
     ,projected_area=0.00014029405053503252
     ,surface_area=0.0004405769537394326
     ,angle_sum=0.2753930632071951
     ,volume=1e-06
     ,sa_to_vol=440.57695373943267
     ,drip_node_id=254
     ,drip_node_loc=(2.181232
     ,2.038962
     ,14.151027))
     ,
Flow(num_cylinders=1
     ,projected_area=0.00035438974889866827
     ,surface_area=0.0011363768946565003
     ,angle_sum=0.2628763885541433
     ,volume=1e-06
     ,sa_to_vol=1136.3768946565003
     ,drip_node_id=259
     ,drip_node_loc=(2.117779
     ,1.893001
     ,14.106881))
     ,
Flow(num_cylinders=2
     ,projected_area=0.0004986408581358576
     ,surface_area=0.001956646736508795
     ,angle_sum=-0.984050403294677
     ,volume=2e-06
     ,sa_to_vol=1956.6467365087951
     ,drip_node_id=262
     ,drip_node_loc=(2.112212
     ,1.941342
     ,14.052377))
     ,
Flow(num_cylinders=1
     ,projected_area=0.0002313219157874267
     ,surface_area=0.0007533696262941004
     ,angle_sum=0.3604125999144887
     ,volume=1e-06
     ,sa_to_vol=753.3696262941004
     ,drip_node_id=274
     ,drip_node_loc=(2.081275
     ,2.440808
     ,14.090243))
     ,
Flow(num_cylinders=0
     ,projected_area=0.0
     ,surface_area=0.0
     ,angle_sum=0.0
     ,volume=0.0
     ,sa_to_vol=0.0
     ,drip_node_id=276
     ,drip_node_loc=(2.043833
     ,2.517283
     ,14.035983))
     ,
Flow(num_cylinders=1
     ,projected_area=0.0003723108777689768
     ,surface_area=0.0019861305835627355
     ,angle_sum=-0.9724871982402891
     ,volume=2e-06
     ,sa_to_vol=993.0652917813678
     ,drip_node_id=304
     ,drip_node_loc=(2.203542
     ,1.577092
     ,13.844742))
     ,
Flow(num_cylinders=4
     ,projected_area=0.0012787894269131134
     ,surface_area=0.004750025260374696
     ,angle_sum=-1.788583466477691
     ,volume=5.999999999999999e-06
     ,sa_to_vol=3360.145400518402
     ,drip_node_id=309
     ,drip_node_loc=(2.111116
     ,1.652066
     ,13.734645))
     ,
Flow(num_cylinders=2
     ,projected_area=0.0005161085845889704
     ,surface_area=0.0019453055870293362
     ,angle_sum=1.2792280411903536
     ,volume=2e-06
     ,sa_to_vol=1945.305587029336
     ,drip_node_id=315
     ,drip_node_loc=(2.209153
     ,1.825379
     ,13.854899))
     ,
Flow(num_cylinders=2
     ,projected_area=0.0005112311572653741
     ,surface_area=0.0017693292745385037
     ,angle_sum=-1.0096884397188939
     ,volume=2e-06
     ,sa_to_vol=698.8001619012458
     ,drip_node_id=320
     ,drip_node_loc=(2.213801
     ,1.740639
     ,13.80634))
     ,
Flow(num_cylinders=1
     ,projected_area=4.043601946826277e-05
     ,surface_area=0.001663049195067561
     ,angle_sum=-1.531460817519031
     ,volume=2e-06
     ,sa_to_vol=831.5245975337806
     ,drip_node_id=322
     ,drip_node_loc=(2.160463
     ,1.791407
     ,13.75528))
     ,
Flow(num_cylinders=0
     ,projected_area=0.0
     ,surface_area=0.0
     ,angle_sum=0.0
     ,volume=0.0
     ,sa_to_vol=0.0
     ,drip_node_id=326
     ,drip_node_loc=(1.842594
     ,1.682903
     ,13.750329))
     ,
Flow(num_cylinders=1
     ,projected_area=0.00024240230040044135
     ,surface_area=0.0007811570133151023
     ,angle_sum=-0.3165665248846151
     ,volume=1e-06
     ,sa_to_vol=781.1570133151023
     ,drip_node_id=327
     ,drip_node_loc=(1.842594
     ,1.682903
     ,13.750329))
     ,
Flow(num_cylinders=3
     ,projected_area=0.0011115028875355593
     ,surface_area=0.0035010536850135377
     ,angle_sum=0.37857258196831484
     ,volume=4.9999999999999996e-06
     ,sa_to_vol=2121.5882048038934
     ,drip_node_id=331
     ,drip_node_loc=(2.035209
     ,1.983062
     ,13.620572))
     ,
Flow(num_cylinders=6
     ,projected_area=0.001610994808148891
     ,surface_area=0.0062853215901840275
     ,angle_sum=2.39032329477659
     ,volume=8e-06
     ,sa_to_vol=5021.985082414331
     ,drip_node_id=334
     ,drip_node_loc=(2.193611
     ,1.903108
     ,13.60279))
     ,
Flow(num_cylinders=2
     ,projected_area=0.00045077592129219417
     ,surface_area=0.002753511713091846
     ,angle_sum=2.068321518216125
     ,volume=4e-06
     ,sa_to_vol=1376.7558565459233
     ,drip_node_id=338
     ,drip_node_loc=(2.282876
     ,1.856895
     ,13.586817))
     ,
Flow(num_cylinders=0
     ,projected_area=0.0
     ,surface_area=0.0
     ,angle_sum=0.0
     ,volume=0.0
     ,sa_to_vol=0.0
     ,drip_node_id=345
     ,drip_node_loc=(2.187081
     ,2.027202
     ,13.612543))
     ,
Flow(num_cylinders=3
     ,projected_area=0.0009134328111442902
     ,surface_area=0.0033080813562667843
     ,angle_sum=1.119601349442374
     ,volume=4e-06
     ,sa_to_vol=2630.6126084834136
     ,drip_node_id=346
     ,drip_node_loc=(2.035209
     ,1.983062
     ,13.620572))
     ,
Flow(num_cylinders=4
     ,projected_area=0.0010470363262884833
     ,surface_area=0.004889951797165585
     ,angle_sum=-3.1445210780616586
     ,volume=6e-06
     ,sa_to_vol=3467.9412984447013
     ,drip_node_id=351
     ,drip_node_loc=(2.023443
     ,1.985047
     ,13.54066))
     ,
Flow(num_cylinders=3
     ,projected_area=0.0010137009936762665
     ,surface_area=0.003234913663364678
     ,angle_sum=-0.13705150606290142
     ,volume=3e-06
     ,sa_to_vol=3234.9136633646785
     ,drip_node_id=354
     ,drip_node_loc=(1.327802
     ,2.458192
     ,13.509324))
     ,
Flow(num_cylinders=13
     ,projected_area=0.003837260621865184
     ,surface_area=0.014614877520058935
     ,angle_sum=7.717613622574722
     ,volume=1.8000000000000004e-05
     ,sa_to_vol=11229.764311926128
     ,drip_node_id=360
     ,drip_node_loc=(1.683417
     ,2.547821
     ,13.594257))
     ,
Flow(num_cylinders=1
     ,projected_area=0.00036062286277023785
     ,surface_area=0.0011935067570620307
     ,angle_sum=-0.3756100213724367
     ,volume=1e-06
     ,sa_to_vol=1193.5067570620308
     ,drip_node_id=366
     ,drip_node_loc=(2.051583
     ,2.639494
     ,13.583351))
     ,
Flow(num_cylinders=6
     ,projected_area=0.0013650461430820568
     ,surface_area=0.005934327150961708
     ,angle_sum=3.1544526648984594
     ,volume=8e-06
     ,sa_to_vol=4669.42770084685
     ,drip_node_id=367
     ,drip_node_loc=(2.059969
     ,2.569309
     ,13.611224))
     ,
Flow(num_cylinders=0
     ,projected_area=0.0
     ,surface_area=0.0
     ,angle_sum=0.0
     ,volume=0.0
     ,sa_to_vol=0.0
     ,drip_node_id=383
     ,drip_node_loc=(1.935376
     ,2.74049
     ,13.691273))
     ,
Flow(num_cylinders=1
     ,projected_area=0.0003856673610054937
     ,surface_area=0.0012405678150128057
     ,angle_sum=0.2717242865353931
     ,volume=2e-06
     ,sa_to_vol=620.2839075064029
     ,drip_node_id=384
     ,drip_node_loc=(1.683417
     ,2.547821
     ,13.594257))
     ,
Flow(num_cylinders=1
     ,projected_area=0.00029546446955781283
     ,surface_area=0.0009470331054246433
     ,angle_sum=0.27480207047244537
     ,volume=1e-06
     ,sa_to_vol=947.0331054246434
     ,drip_node_id=386
     ,drip_node_loc=(1.696362
     ,2.678336
     ,13.595628))
     ,
Flow(num_cylinders=0
     ,projected_area=0.0
     ,surface_area=0.0
     ,angle_sum=0.0
     ,volume=0.0
     ,sa_to_vol=0.0
     ,drip_node_id=388
     ,drip_node_loc=(1.627908
     ,2.790386
     ,13.592906))
     ,
Flow(num_cylinders=6
     ,projected_area=0.0018491015574594882
     ,surface_area=0.007099983689149665
     ,angle_sum=2.8897427389613988
     ,volume=9.999999999999999e-06
     ,sa_to_vol=4632.498279203902
     ,drip_node_id=389
     ,drip_node_loc=(1.52335
     ,2.452157
     ,13.506494))
     ,
Flow(num_cylinders=3
     ,projected_area=0.0008680501936671784
     ,surface_area=0.0027944466653681216
     ,angle_sum=-0.5404382986711217
     ,volume=3e-06
     ,sa_to_vol=2794.4466653681216
     ,drip_node_id=395
     ,drip_node_loc=(1.796062
     ,2.239466
     ,13.313719))
     ,
Flow(num_cylinders=5
     ,projected_area=0.0014878231569296014
     ,surface_area=0.00560139686949753
     ,angle_sum=2.4250494997819736
     ,volume=7e-06
     ,sa_to_vol=4095.301643403315
     ,drip_node_id=397
     ,drip_node_loc=(1.87309
     ,2.183421
     ,13.265917))
     ,
Flow(num_cylinders=3
     ,projected_area=0.0008636103785011247
     ,surface_area=0.003072870314292517
     ,angle_sum=-0.47743068181052684
     ,volume=4e-06
     ,sa_to_vol=2345.4973672068722
     ,drip_node_id=406
     ,drip_node_loc=(1.931817
     ,2.350368
     ,13.193707))
     ,
Flow(num_cylinders=4
     ,projected_area=0.0008727672494955126
     ,surface_area=0.004371934584515165
     ,angle_sum=-3.5439720195007043
     ,volume=4e-06
     ,sa_to_vol=4371.934584515165
     ,drip_node_id=409
     ,drip_node_loc=(1.733348
     ,2.273245
     ,13.274314))
     ,
Flow(num_cylinders=1
     ,projected_area=0.0005508568154471113
     ,surface_area=0.0017525862444557909
     ,angle_sum=0.21437515945434096
     ,volume=3e-06
     ,sa_to_vol=584.195414818597
     ,drip_node_id=429
     ,drip_node_loc=(1.703653
     ,3.142939
     ,13.261127))
     ,
Flow(num_cylinders=4
     ,projected_area=0.001735623156265729
     ,surface_area=0.005476392897811192
     ,angle_sum=0.20973989897871803
     ,volume=6.999999999999999e-06
     ,sa_to_vol=3124.753716966552
     ,drip_node_id=432
     ,drip_node_loc=(1.79801
     ,3.212342
     ,13.258305))
     ,
Flow(num_cylinders=3
     ,projected_area=0.001168776201792099
     ,surface_area=0.004582625495828164
     ,angle_sum=0.6787966608368236
     ,volume=5.999999999999999e-06
     ,sa_to_vol=2420.2096764969933
     ,drip_node_id=437
     ,drip_node_loc=(1.899537
     ,3.500702
     ,13.081461))
     ,
Flow(num_cylinders=5
     ,projected_area=0.0017827246977828253
     ,surface_area=0.005761445307234662
     ,angle_sum=0.801423121000973
     ,volume=6.999999999999999e-06
     ,sa_to_vol=4185.4025207082705
     ,drip_node_id=440
     ,drip_node_loc=(2.005679
     ,3.65546
     ,13.096724))
     ,
Flow(num_cylinders=2
     ,projected_area=0.00044579203368799963
     ,surface_area=0.0015490879215585914
     ,angle_sum=-0.05307055623179707
     ,volume=2e-06
     ,sa_to_vol=1549.0879215585915
     ,drip_node_id=447
     ,drip_node_loc=(1.853544
     ,3.991946
     ,13.109796))
     ,
Flow(num_cylinders=1
     ,projected_area=0.0003559737811697003
     ,surface_area=0.0011266693733569075
     ,angle_sum=-0.18806897721333118
     ,volume=1e-06
     ,sa_to_vol=1126.6693733569075
     ,drip_node_id=450
     ,drip_node_loc=(1.903905
     ,3.989086
     ,13.127798))
     ,
Flow(num_cylinders=4
     ,projected_area=0.0018014451105333635
     ,surface_area=0.005735888450997709
     ,angle_sum=-0.7935819300671257
     ,volume=6.999999999999999e-06
     ,sa_to_vol=3117.420716114298
     ,drip_node_id=452
     ,drip_node_loc=(2.009576
     ,3.334709
     ,13.132934))
     ,
Flow(num_cylinders=2
     ,projected_area=0.0006624993756169215
     ,surface_area=0.002499780982424667
     ,angle_sum=-0.8299268862915081
     ,volume=3e-06
     ,sa_to_vol=1832.6088045634363
     ,drip_node_id=457
     ,drip_node_loc=(1.873033
     ,3.203683
     ,13.207621))
     ,
Flow(num_cylinders=0
     ,projected_area=0.0
     ,surface_area=0.0
     ,angle_sum=0.0
     ,volume=0.0
     ,sa_to_vol=0.0
     ,drip_node_id=459
     ,drip_node_loc=(2.002488
     ,3.222128
     ,13.158594))
     ,
Flow(num_cylinders=12
     ,projected_area=0.00540908851933797
     ,surface_area=0.01802621446286764
     ,angle_sum=-0.4787582368320998
     ,volume=2.6000000000000005e-05
     ,sa_to_vol=9243.690988078295
     ,drip_node_id=462
     ,drip_node_loc=(1.483922
     ,3.091829
     ,13.085572))
     ,
Flow(num_cylinders=1
     ,projected_area=0.00024067942976821222
     ,surface_area=0.0007546890952086082
     ,angle_sum=-0.13480399474412763
     ,volume=1e-06
     ,sa_to_vol=754.6890952086081
     ,drip_node_id=466
     ,drip_node_loc=(1.265089
     ,2.964109
     ,13.077723))
     ,
Flow(num_cylinders=0
     ,projected_area=0.0
     ,surface_area=0.0
     ,angle_sum=0.0
     ,volume=0.0
     ,sa_to_vol=0.0
     ,drip_node_id=474
     ,drip_node_loc=(1.508873
     ,3.185036
     ,13.428693))
     ,
Flow(num_cylinders=1
     ,projected_area=0.0002845057304893031
     ,surface_area=0.000891725366758195
     ,angle_sum=-0.06100468401593667
     ,volume=1e-06
     ,sa_to_vol=891.725366758195
     ,drip_node_id=478
     ,drip_node_loc=(1.461031
     ,3.108335
     ,13.327606))
     ,
Flow(num_cylinders=4
     ,projected_area=0.001392285291196621
     ,surface_area=0.0050440312088608965
     ,angle_sum=1.7837484177100857
     ,volume=6.999999999999999e-06
     ,sa_to_vol=2799.033390642362
     ,drip_node_id=482
     ,drip_node_loc=(1.561669
     ,3.037909
     ,13.267448))
     ,
Flow(num_cylinders=13
     ,projected_area=0.0034617049233297155
     ,surface_area=0.014428530326413332
     ,angle_sum=6.272651295534475
     ,volume=2.1000000000000002e-05
     ,sa_to_vol=9929.324154497303
     ,drip_node_id=487
     ,drip_node_loc=(1.382266
     ,3.06225
     ,13.227227))
     ,
Flow(num_cylinders=1
     ,projected_area=0.00026485421826719514
     ,surface_area=0.0013234901531043082
     ,angle_sum=0.9383782899612891
     ,volume=2e-06
     ,sa_to_vol=661.7450765521542
     ,drip_node_id=499
     ,drip_node_loc=(1.58826
     ,2.548049
     ,13.013078))
     ,
Flow(num_cylinders=5
     ,projected_area=0.0012509280124092987
     ,surface_area=0.004416482368343067
     ,angle_sum=0.9546746455068511
     ,volume=4.9999999999999996e-06
     ,sa_to_vol=4416.482368343068
     ,drip_node_id=503
     ,drip_node_loc=(1.58826
     ,2.548049
     ,13.013078))
     ,
Flow(num_cylinders=1
     ,projected_area=0.000311559880414428
     ,surface_area=0.00100832557809618
     ,angle_sum=0.31113909139565027
     ,volume=1e-06
     ,sa_to_vol=1008.3255780961802
     ,drip_node_id=513
     ,drip_node_loc=(1.517831
     ,2.821892
     ,12.982214))
     ,
Flow(num_cylinders=24
     ,projected_area=0.008381438510571272
     ,surface_area=0.03232846927681765
     ,angle_sum=1.6972430927750466
     ,volume=5.4e-05
     ,sa_to_vol=18378.751295591734
     ,drip_node_id=515
     ,drip_node_loc=(1.517831
     ,2.821892
     ,12.982214))]



drip_mid_flows = [Flow(num_cylinders=117, projected_area=16.47655636448612, surface_area=19.350321212472778, angle_sum=134.88157931803016, volume=3.906033, sa_to_vol=7306.133204864248, drip_node_id=0, drip_node_loc=(-0.299115, 2.537844)), Flow(num_cylinders=13, projected_area=0.00923207646440376, surface_area=0.03283550215579902, angle_sum=9.192417456046483, volume=0.00010000000000000002, sa_to_vol=4584.585465214609, drip_node_id=117, drip_node_loc=(0.953051, 2.49861, 13.300944))]



drip_adj_flows = [
    Flow(
        num_cylinders=107,
        projected_area=2.9604039491372682,
        surface_area=7.394338347069087,
        angle_sum=124.04233409518383,
        volume=0.521757,
        sa_to_vol=4664.192277179154,
        drip_node_id=0,
        drip_node_loc=(0.076822, -3.386935),
    ),
    Flow(
        num_cylinders=9,
        projected_area=0.004525372650859205,
        surface_area=0.021259069308619528,
        angle_sum=7.520595686565588,
        volume=3.5999999999999994e-05,
        sa_to_vol=6496.681010422562,
        drip_node_id=125,
        drip_node_loc=(-0.363553, -1.01903, 10.495052),
    ),
]

ten_cyls_edges = [
    (0.0, -1.0),
    (0.0, 1.0),
    (1.0, 2.0),
    (2.0, 3.0),
    (3.0, 4.0),
    (4.0, 5.0),
    (5.0, 6.0),
    (6.0, 7.0),
    (7.0, 8.0),
    (8.0, 9.0),
]

happy_path_edges = [
    (0.0, -1.0),
    (0.0, 1.0),
    (1.0, 2.0),
    (2.0, 3.0),
    (3.0, 4.0),
    (4.0, 5.0),
    (5.0, 6.0),
    (6.0, 7.0),
    (7.0, 8.0),
    (8.0, 9.0),
    (9.0, 10.0),
    (10.0, 11.0),
    (11.0, 12.0),
    (12.0, 13.0),
    (13.0, 14.0),
    (14.0, 15.0),
    (15.0, 16.0),
    (16.0, 17.0),
    (17.0, 18.0),
    (18.0, 19.0),
    (19.0, 20.0),
    (20.0, 21.0),
    (21.0, 22.0),
    (22.0, 23.0),
    (23.0, 24.0),
    (24.0, 25.0),
    (25.0, 26.0),
    (26.0, 27.0),
    (27.0, 28.0),
    (28.0, 29.0),
    (29.0, 30.0),
    (30.0, 31.0),
    (31.0, 32.0),
    (32.0, 33.0),
    (33.0, 34.0),
    (34.0, 35.0),
    (35.0, 36.0),
    (36.0, 37.0),
    (37.0, 38.0),
    (38.0, 39.0),
    (39.0, 40.0),
    (40.0, 41.0),
    (41.0, 42.0),
    (42.0, 43.0),
    (43.0, 44.0),
    (44.0, 45.0),
    (45.0, 46.0),
    (46.0, 47.0),
    (47.0, 48.0),
    (48.0, 49.0),
    (49.0, 50.0),
    (50.0, 51.0),
    (51.0, 52.0),
    (52.0, 53.0),
    (53.0, 54.0),
    (54.0, 55.0),
    (55.0, 56.0),
    (56.0, 57.0),
    (57.0, 58.0),
    (58.0, 59.0),
    (59.0, 60.0),
    (60.0, 61.0),
    (61.0, 62.0),
    (62.0, 63.0),
    (63.0, 64.0),
    (64.0, 65.0),
    (65.0, 66.0),
    (66.0, 67.0),
    (67.0, 68.0),
    (68.0, 69.0),
    (69.0, 70.0),
    (70.0, 71.0),
    (71.0, 72.0),
    (72.0, 73.0),
    (73.0, 74.0),
    (74.0, 75.0),
    (75.0, 76.0),
    (76.0, 77.0),
    (77.0, 78.0),
    (78.0, 79.0),
    (79.0, 80.0),
    (80.0, 81.0),
    (81.0, 82.0),
    (82.0, 83.0),
    (83.0, 84.0),
    (84.0, 85.0),
    (85.0, 86.0),
    (86.0, 87.0),
    (87.0, 88.0),
    (88.0, 89.0),
    (89.0, 90.0),
    (90.0, 91.0),
    (91.0, 92.0),
    (92.0, 93.0),
    (93.0, 94.0),
    (94.0, 95.0),
    (95.0, 96.0),
    (96.0, 97.0),
    (97.0, 98.0),
    (98.0, 99.0),
    (99.0, 100.0),
    (100.0, 101.0),
    (101.0, 102.0),
    (102.0, 103.0),
    (102.0, 148.0),
    (103.0, 104.0),
    (104.0, 105.0),
    (104.0, 138.0),
    (105.0, 106.0),
    (138.0, 139.0),
    (139.0, 140.0),
    (140.0, 141.0),
    (141.0, 142.0),
    (142.0, 143.0),
    (143.0, 144.0),
    (144.0, 145.0),
    (145.0, 146.0),
    (146.0, 147.0),
    (148.0, 149.0),
    (149.0, 150.0),
]

small_tree_edges = [
    (0.0, -1.0),
    (0.0, 1.0),
    (1.0, 2.0),
    (2.0, 3.0),
    (3.0, 4.0),
    (4.0, 5.0),
    (5.0, 6.0),
    (6.0, 7.0),
    (7.0, 8.0),
    (8.0, 9.0),
    (9.0, 10.0),
    (10.0, 11.0),
    (11.0, 12.0),
    (12.0, 13.0),
    (13.0, 14.0),
    (14.0, 15.0),
    (15.0, 16.0),
    (16.0, 17.0),
    (17.0, 18.0),
    (18.0, 19.0),
    (19.0, 20.0),
    (20.0, 21.0),
    (21.0, 22.0),
    (22.0, 23.0),
    (23.0, 24.0),
    (24.0, 25.0),
    (25.0, 26.0),
    (26.0, 27.0),
    (27.0, 28.0),
    (28.0, 29.0),
    (29.0, 30.0),
    (30.0, 31.0),
    (31.0, 32.0),
    (32.0, 33.0),
    (33.0, 34.0),
    (34.0, 35.0),
    (35.0, 36.0),
    (36.0, 37.0),
    (37.0, 38.0),
    (38.0, 39.0),
    (39.0, 40.0),
    (40.0, 41.0),
    (41.0, 42.0),
    (42.0, 43.0),
    (43.0, 44.0),
    (44.0, 45.0),
    (45.0, 46.0),
    (46.0, 47.0),
    (47.0, 48.0),
    (48.0, 49.0),
    (49.0, 50.0),
    (50.0, 51.0),
    (51.0, 52.0),
    (52.0, 53.0),
    (53.0, 54.0),
    (54.0, 55.0),
    (55.0, 56.0),
    (56.0, 57.0),
    (57.0, 58.0),
    (58.0, 59.0),
    (59.0, 60.0),
    (60.0, 61.0),
    (61.0, 62.0),
    (62.0, 63.0),
    (63.0, 64.0),
    (64.0, 65.0),
    (65.0, 66.0),
    (66.0, 67.0),
    (67.0, 68.0),
    (68.0, 69.0),
    (69.0, 70.0),
    (70.0, 71.0),
    (71.0, 72.0),
    (72.0, 73.0),
    (73.0, 74.0),
    (74.0, 75.0),
    (75.0, 76.0),
    (76.0, 77.0),
    (77.0, 78.0),
    (78.0, 79.0),
    (79.0, 80.0),
    (80.0, 81.0),
    (81.0, 82.0),
    (82.0, 83.0),
    (83.0, 84.0),
    (84.0, 85.0),
    (85.0, 86.0),
    (86.0, 87.0),
    (87.0, 88.0),
    (88.0, 89.0),
    (89.0, 90.0),
    (90.0, 91.0),
    (91.0, 92.0),
    (92.0, 93.0),
    (93.0, 94.0),
    (94.0, 95.0),
    (95.0, 96.0),
    (96.0, 97.0),
    (97.0, 98.0),
    (98.0, 99.0),
    (99.0, 100.0),
    (100.0, 101.0),
    (101.0, 102.0),
    (102.0, 103.0),
    (103.0, 104.0),
    (104.0, 105.0),
    (105.0, 106.0),
    (106.0, 107.0),
    (107.0, 108.0),
    (108.0, 109.0),
    (109.0, 110.0),
    (110.0, 111.0),
    (111.0, 112.0),
    (112.0, 113.0),
    (113.0, 114.0),
    (114.0, 115.0),
    (115.0, 116.0),
    (116.0, 117.0),
    (117.0, 118.0),
    (117.0, 412.0),
    (118.0, 119.0),
    (119.0, 120.0),
    (120.0, 121.0),
    (121.0, 122.0),
    (122.0, 123.0),
    (122.0, 353.0),
    (123.0, 124.0),
    (124.0, 125.0),
    (125.0, 126.0),
    (126.0, 127.0),
    (126.0, 277.0),
    (127.0, 128.0),
    (128.0, 129.0),
    (129.0, 130.0),
    (130.0, 131.0),
    (130.0, 228.0),
    (131.0, 132.0),
    (132.0, 133.0),
    (133.0, 134.0),
    (133.0, 224.0),
    (133.0, 226.0),
    (134.0, 135.0),
    (134.0, 192.0),
    (135.0, 136.0),
    (136.0, 137.0),
    (137.0, 138.0),
    (138.0, 139.0),
    (138.0, 190.0),
    (139.0, 140.0),
    (139.0, 165.0),
    (139.0, 186.0),
    (140.0, 141.0),
    (140.0, 155.0),
    (141.0, 142.0),
    (142.0, 143.0),
    (143.0, 144.0),
    (143.0, 152.0),
    (144.0, 145.0),
    (145.0, 146.0),
    (145.0, 149.0),
    (145.0, 151.0),
    (146.0, 147.0),
    (147.0, 148.0),
    (149.0, 150.0),
    (152.0, 153.0),
    (153.0, 154.0),
    (155.0, 156.0),
    (156.0, 157.0),
    (157.0, 158.0),
    (158.0, 159.0),
    (159.0, 160.0),
    (160.0, 161.0),
    (161.0, 162.0),
    (162.0, 163.0),
    (163.0, 164.0),
    (165.0, 166.0),
    (165.0, 177.0),
    (165.0, 184.0),
    (166.0, 167.0),
    (167.0, 168.0),
    (168.0, 169.0),
    (168.0, 174.0),
    (169.0, 170.0),
    (169.0, 172.0),
    (170.0, 171.0),
    (172.0, 173.0),
    (174.0, 175.0),
    (175.0, 176.0),
    (177.0, 178.0),
    (178.0, 179.0),
    (179.0, 180.0),
    (180.0, 181.0),
    (181.0, 182.0),
    (182.0, 183.0),
    (184.0, 185.0),
    (186.0, 187.0),
    (187.0, 188.0),
    (188.0, 189.0),
    (190.0, 191.0),
    (192.0, 193.0),
    (192.0, 222.0),
    (193.0, 194.0),
    (194.0, 195.0),
    (195.0, 196.0),
    (196.0, 197.0),
    (196.0, 220.0),
    (197.0, 198.0),
    (198.0, 199.0),
    (199.0, 200.0),
    (199.0, 214.0),
    (200.0, 201.0),
    (201.0, 202.0),
    (201.0, 212.0),
    (202.0, 203.0),
    (203.0, 204.0),
    (204.0, 205.0),
    (204.0, 209.0),
    (205.0, 206.0),
    (206.0, 207.0),
    (207.0, 208.0),
    (209.0, 210.0),
    (210.0, 211.0),
    (212.0, 213.0),
    (214.0, 215.0),
    (215.0, 216.0),
    (215.0, 218.0),
    (216.0, 217.0),
    (218.0, 219.0),
    (220.0, 221.0),
    (222.0, 223.0),
    (224.0, 225.0),
    (226.0, 227.0),
    (228.0, 229.0),
    (229.0, 230.0),
    (229.0, 267.0),
    (230.0, 231.0),
    (231.0, 232.0),
    (232.0, 233.0),
    (233.0, 234.0),
    (234.0, 235.0),
    (235.0, 236.0),
    (235.0, 256.0),
    (235.0, 263.0),
    (236.0, 237.0),
    (236.0, 253.0),
    (237.0, 238.0),
    (238.0, 239.0),
    (239.0, 240.0),
    (240.0, 241.0),
    (240.0, 251.0),
    (241.0, 242.0),
    (242.0, 243.0),
    (242.0, 249.0),
    (243.0, 244.0),
    (244.0, 245.0),
    (245.0, 246.0),
    (245.0, 248.0),
    (246.0, 247.0),
    (249.0, 250.0),
    (251.0, 252.0),
    (253.0, 254.0),
    (254.0, 255.0),
    (256.0, 257.0),
    (257.0, 258.0),
    (257.0, 261.0),
    (258.0, 259.0),
    (259.0, 260.0),
    (261.0, 262.0),
    (263.0, 264.0),
    (264.0, 265.0),
    (265.0, 266.0),
    (267.0, 268.0),
    (268.0, 269.0),
    (269.0, 270.0),
    (270.0, 271.0),
    (271.0, 272.0),
    (272.0, 273.0),
    (273.0, 274.0),
    (274.0, 275.0),
    (275.0, 276.0),
    (277.0, 278.0),
    (278.0, 279.0),
    (279.0, 280.0),
    (280.0, 281.0),
    (281.0, 282.0),
    (282.0, 283.0),
    (283.0, 284.0),
    (284.0, 285.0),
    (284.0, 328.0),
    (284.0, 352.0),
    (285.0, 286.0),
    (285.0, 323.0),
    (286.0, 287.0),
    (287.0, 288.0),
    (287.0, 312.0),
    (288.0, 289.0),
    (288.0, 300.0),
    (288.0, 307.0),
    (289.0, 290.0),
    (290.0, 291.0),
    (291.0, 292.0),
    (291.0, 298.0),
    (292.0, 293.0),
    (293.0, 294.0),
    (294.0, 295.0),
    (295.0, 296.0),
    (296.0, 297.0),
    (298.0, 299.0),
    (300.0, 301.0),
    (301.0, 302.0),
    (302.0, 303.0),
    (302.0, 305.0),
    (303.0, 304.0),
    (305.0, 306.0),
    (307.0, 308.0),
    (308.0, 309.0),
    (309.0, 310.0),
    (310.0, 311.0),
    (312.0, 313.0),
    (313.0, 314.0),
    (313.0, 318.0),
    (313.0, 321.0),
    (314.0, 315.0),
    (315.0, 316.0),
    (316.0, 317.0),
    (318.0, 319.0),
    (319.0, 320.0),
    (321.0, 322.0),
    (323.0, 324.0),
    (324.0, 325.0),
    (325.0, 326.0),
    (325.0, 327.0),
    (328.0, 329.0),
    (329.0, 330.0),
    (330.0, 331.0),
    (330.0, 346.0),
    (330.0, 350.0),
    (331.0, 332.0),
    (332.0, 333.0),
    (332.0, 344.0),
    (333.0, 334.0),
    (334.0, 335.0),
    (334.0, 339.0),
    (334.0, 342.0),
    (335.0, 336.0),
    (335.0, 338.0),
    (336.0, 337.0),
    (339.0, 340.0),
    (340.0, 341.0),
    (342.0, 343.0),
    (344.0, 345.0),
    (346.0, 347.0),
    (347.0, 348.0),
    (348.0, 349.0),
    (350.0, 351.0),
    (353.0, 354.0),
    (354.0, 355.0),
    (355.0, 356.0),
    (356.0, 357.0),
    (356.0, 389.0),
    (356.0, 410.0),
    (357.0, 358.0),
    (358.0, 359.0),
    (359.0, 360.0),
    (359.0, 384.0),
    (360.0, 361.0),
    (360.0, 373.0),
    (361.0, 362.0),
    (362.0, 363.0),
    (363.0, 364.0),
    (363.0, 371.0),
    (364.0, 365.0),
    (364.0, 367.0),
    (364.0, 369.0),
    (365.0, 366.0),
    (367.0, 368.0),
    (369.0, 370.0),
    (371.0, 372.0),
    (373.0, 374.0),
    (374.0, 375.0),
    (375.0, 376.0),
    (375.0, 382.0),
    (376.0, 377.0),
    (377.0, 378.0),
    (378.0, 379.0),
    (378.0, 381.0),
    (379.0, 380.0),
    (382.0, 383.0),
    (384.0, 385.0),
    (385.0, 386.0),
    (386.0, 387.0),
    (387.0, 388.0),
    (389.0, 390.0),
    (390.0, 391.0),
    (391.0, 392.0),
    (392.0, 393.0),
    (393.0, 394.0),
    (393.0, 408.0),
    (394.0, 395.0),
    (395.0, 396.0),
    (395.0, 403.0),
    (396.0, 397.0),
    (396.0, 401.0),
    (397.0, 398.0),
    (398.0, 399.0),
    (399.0, 400.0),
    (401.0, 402.0),
    (403.0, 404.0),
    (403.0, 407.0),
    (404.0, 405.0),
    (405.0, 406.0),
    (408.0, 409.0),
    (410.0, 411.0),
    (412.0, 413.0),
    (413.0, 414.0),
    (414.0, 415.0),
    (415.0, 416.0),
    (416.0, 417.0),
    (417.0, 418.0),
    (418.0, 419.0),
    (418.0, 490.0),
    (419.0, 420.0),
    (420.0, 421.0),
    (421.0, 422.0),
    (422.0, 423.0),
    (423.0, 424.0),
    (423.0, 470.0),
    (423.0, 487.0),
    (424.0, 425.0),
    (424.0, 460.0),
    (425.0, 426.0),
    (426.0, 427.0),
    (427.0, 428.0),
    (428.0, 429.0),
    (429.0, 430.0),
    (430.0, 431.0),
    (430.0, 456.0),
    (431.0, 432.0),
    (431.0, 454.0),
    (432.0, 433.0),
    (433.0, 434.0),
    (434.0, 435.0),
    (434.0, 453.0),
    (435.0, 436.0),
    (435.0, 451.0),
    (436.0, 437.0),
    (437.0, 438.0),
    (438.0, 439.0),
    (439.0, 440.0),
    (440.0, 441.0),
    (441.0, 442.0),
    (442.0, 443.0),
    (443.0, 444.0),
    (444.0, 445.0),
    (445.0, 446.0),
    (445.0, 449.0),
    (446.0, 447.0),
    (447.0, 448.0),
    (449.0, 450.0),
    (451.0, 452.0),
    (454.0, 455.0),
    (456.0, 457.0),
    (457.0, 458.0),
    (458.0, 459.0),
    (460.0, 461.0),
    (461.0, 462.0),
    (462.0, 463.0),
    (463.0, 464.0),
    (463.0, 468.0),
    (464.0, 465.0),
    (465.0, 466.0),
    (466.0, 467.0),
    (468.0, 469.0),
    (470.0, 471.0),
    (470.0, 480.0),
    (471.0, 472.0),
    (471.0, 475.0),
    (471.0, 478.0),
    (472.0, 473.0),
    (473.0, 474.0),
    (475.0, 476.0),
    (476.0, 477.0),
    (478.0, 479.0),
    (480.0, 481.0),
    (481.0, 482.0),
    (482.0, 483.0),
    (483.0, 484.0),
    (484.0, 485.0),
    (485.0, 486.0),
    (487.0, 488.0),
    (488.0, 489.0),
    (490.0, 491.0),
    (491.0, 492.0),
    (492.0, 493.0),
    (492.0, 516.0),
    (493.0, 494.0),
    (493.0, 508.0),
    (494.0, 495.0),
    (495.0, 496.0),
    (495.0, 504.0),
    (496.0, 497.0),
    (497.0, 498.0),
    (498.0, 499.0),
    (498.0, 501.0),
    (498.0, 503.0),
    (499.0, 500.0),
    (501.0, 502.0),
    (504.0, 505.0),
    (505.0, 506.0),
    (506.0, 507.0),
    (508.0, 509.0),
    (509.0, 510.0),
    (509.0, 513.0),
    (509.0, 515.0),
    (510.0, 511.0),
    (511.0, 512.0),
    (513.0, 514.0),
]

drip_on_trunk_flows = [Flow(num_cylinders=100, projected_area=18.585135753681307, surface_area=22.124462796803396, angle_sum=121.15837282927401, volume=4.300205, sa_to_vol=1486.9747724424142, drip_node_id=0, drip_node_loc=(0.04115, -3.741772)), Flow(num_cylinders=13, projected_area=0.43239435949564625, surface_area=1.0369146690952122, angle_sum=10.389951556522455, volume=0.042569, sa_to_vol=303.40831542133907, drip_node_id=100, drip_node_loc=(-2.392058, -2.902613, 12.389604)), Flow(num_cylinders=4, projected_area=0.04253631579360222, surface_area=0.14724832805518684, angle_sum=-2.045982924572768, volume=0.0016970000000000002, sa_to_vol=392.9840386727017, drip_node_id=117, drip_node_loc=(-1.246214, -2.210357, 13.052035)), Flow(num_cylinders=1, projected_area=0.00021179824861767587, surface_area=0.001324212719414634, angle_sum=-1.0915167226038351, volume=2e-06, sa_to_vol=662.106359707317, drip_node_id=150, drip_node_loc=(-2.064803, -1.364778, 14.436379)), Flow(num_cylinders=3, projected_area=0.001048206061783359, surface_area=0.0043425606932041, angle_sum=-2.2774165493165968, volume=4.9999999999999996e-06, sa_to_vol=2750.786381464857, drip_node_id=170, drip_node_loc=(-1.362748, -1.510724, 13.418749)), Flow(num_cylinders=4, projected_area=0.00136015074752023, surface_area=0.006079954654259658, angle_sum=-2.050096449760949, volume=9e-06, sa_to_vol=2615.399190018604, drip_node_id=173, drip_node_loc=(-1.478484, -1.700226, 13.190205)), Flow(num_cylinders=5, projected_area=0.0019042467668787112, surface_area=0.008822990180010988, angle_sum=-1.5016645013682752, volume=9.999999999999999e-06, sa_to_vol=4653.669995695219, drip_node_id=179, drip_node_loc=(-1.224836, -1.951785, 12.882517)), Flow(num_cylinders=61, projected_area=0.06293255184998608, surface_area=0.2603148513086288, angle_sum=44.19360857083035, volume=0.0014929999999999998, sa_to_vol=35411.61393642259, drip_node_id=197, drip_node_loc=(-1.163792, -2.450002, 12.598542))]


ten_cyls_dbh = 0.37489
happy_path_dbh = 0.37489
small_tree_dbh = 1.058276
