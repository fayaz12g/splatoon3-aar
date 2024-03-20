
def create_visuals(do_screenshot, do_disable_fxaa, do_disable_dynamicres, do_disable_dof, do_disable_bloom):

    screenshot = "disabled"
    disablefxaa = "disabled"
    disabledynamicres = "disabled"
    disabledof = "disabled"
    disablebloom = "disabled"

    do_island = False
    
    visual_fixes = []

    if do_screenshot:
        screenshot = "enabled"
    if do_disable_fxaa:
        disablefxaa = "enabled"
    if do_disable_dynamicres:
        disabledynamicres = "enabled"
    if do_disable_dof:
        disabledof = "enabled"
    if do_disable_bloom:
        disablebloom = "enabled"
        
    visuals6_0_2 = f'''// 2580x1080 Docked
@{screenshot}
04c5f210 8A42C1F2
@stop

// 60FPS
@{disablefxaa}
0412e940 480D1E32
0412e868 480D1E32
0412e390 480D1E32
0412d798 480D1E32
0235614c 480D1E32
0161adbc 480D1E32
0161ad10 480D1E32
015df844 480D1E32
01187ef0 480D1E32
01186d60 480D1E32
@stop
'''


    visuals7_0_0 = f'''// 2580x1080 Docked
@{do_screenshot}
04c5f210 8A42C1F2
@stop

// 60FPS
@{disablefxaa}
0412e940 480D1E32
0412e868 480D1E32
0412e390 480D1E32
0412d798 480D1E32
0235614c 480D1E32
0161adbc 480D1E32
0161ad10 480D1E32
015df844 480D1E32
01187ef0 480D1E32
01186d60 480D1E32
@stop
'''

    visual_fixes.append(visuals6_0_2)
    visual_fixes.append(visuals7_0_0)
    
    return visual_fixes