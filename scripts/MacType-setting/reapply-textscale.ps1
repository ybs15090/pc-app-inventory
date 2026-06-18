# 等待 MacType 完成初始化（RedrawDelay=5000，多等几秒确保完成）
Start-Sleep -Seconds 8

# 确保注册表值为 120
$key = "HKCU:\Software\Microsoft\Accessibility"
Set-ItemProperty -Path $key -Name TextScaleFactor -Value 120 -Type DWord

# 广播 WM_SETTINGCHANGE 通知所有窗口重新读取设置
Add-Type -TypeDefinition @"
using System;
using System.Runtime.InteropServices;
public class WinMsg {
    [DllImport("user32.dll", CharSet = CharSet.Auto)]
    public static extern IntPtr SendMessageTimeout(IntPtr hWnd, uint Msg, UIntPtr wParam,
        string lParam, uint fuFlags, uint uTimeout, out UIntPtr lpdwResult);
}
"@
$result = [UIntPtr]::Zero
[WinMsg]::SendMessageTimeout([IntPtr]0xffff, 0x001A, [UIntPtr]::Zero, "ImmersiveColorSet", 0x0002, 5000, [ref]$result) | Out-Null
