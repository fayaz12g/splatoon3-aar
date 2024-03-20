import os
import math

def create_patch_files(patch_folder, ratio_value, scaling_factor, visual_fixes):

    def make_hex(x, r):
        p = math.floor(math.log(x, 2))
        a = round(16*(p-2) + x / 2**(p-4))
        if a<0: a += 128
        a = 2*a + 1
        h = hex(a).lstrip('0x').rjust(2,'0').upper()
        hex_value = f'0{r}' + h[1] + '02' + h[0] + '1E' 
        print(hex_value)
        return hex_value

    visual_fixesa = visual_fixes[0]
    visual_fixesb = visual_fixes[1]
    scaling_factor = float(scaling_factor)
    ratio_value = float(ratio_value)
    print(f"The scaling factor is {scaling_factor}.")
    hex_value = make_hex(ratio_value, 0)
    hex_value2 = make_hex(ratio_value, 3)
    version_variables = ["6.0.2", "7.0.0"]
    for version_variable in version_variables:
        file_name = f"main-{version_variable}.pchtxt"
        file_path = os.path.join(patch_folder, file_name)

        if version_variable == "6.0.2":
            nsobidid = "07D15286943ED1C35B22D34B465734FE9E3B3AD7"
            # replacement_value = "008FADE0"
            # replacement2_value = "009692D0"
            visual_fix = visual_fixesa

        elif version_variable == "7.0.0":
            nsobidid = "B719E1205BC5B5E8C5EE1734AF5F48730C94A92B"
            # replacement_value = "008FADE0"
            # replacement2_value = "009692D0"
            visual_fix = visual_fixesb

        patch_content = f'''@nsobid-{nsobidid}

@flag print_values
@flag offset_shift 0x100

@enabled
011BA334 DE719C52
011BA338 1E03A872
011BA33C C003271E
055A3040 0A03A872
028FA588 0803A872
028FA948 0803A872
02B1AD50 0803A872
02B1B9C8 0803A872
02D08734 0803A872
04F18AA0 0103E8F2
04E8F934 0303E8F2
012EF66C 0803E8F2
02AE14F8 0803E8F2
04F3A0E4 0803E8F2
04F41EC0 0803E8F2
04E7ED98 0903E8F2
04E9DF0C 0903E8F2
04FB3100 0903E8F2
02B11B14 0A03A872
05607260 0A03A872
02B14ACC 0C03A872
04E7EE94 0C03A872
04F39EFC 0D03A872
04F396CC 0E03A872
011B9920 1003A872
027C10A4 0A03A8F2
0197A20C 0A03E8F2
0187CAA0 0803A8F2
01814FBC 0903E8F2
01814FBC 0903E8F2
@stop

{visual_fix}

// Generated using SPLATOON3-AAR by Fayaz (github.com/fayaz12g/splatoon3-aar)
// Non 21:9 AR coming soon
// Made possible by Fl4sh_#9174'''
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as patch_file:
            patch_file.write(patch_content)
        print(f"Patch file created: {file_path}")
