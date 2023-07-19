import pyaudio

p = pyaudio.PyAudio()

device_info = p.get_device_info_by_index(7)  # 0はデバイスIDを指す。必要に応じて適切なIDに置き換えてください。

# 最大サンプルレートを取得します。
max_rate = device_info['defaultSampleRate']

print("Default Sample Rate: ", max_rate)

# 可能なサンプルレートを調べるために、一般的なサンプルレートでデバイスを開く試みます。
for test_rate in [8000, 11025, 16000, 22050, 44100, 48000, 96000, 192000]:
    try:
        is_rate_supported = p.is_format_supported(test_rate,  # 試すサンプルレート
                                                  input_device=device_info['index'],  # デバイスID
                                                  input_channels=device_info['maxInputChannels'],  # 入力チャネル数
                                                  input_format=pyaudio.paInt16)  # 入力フォーマット
    except ValueError:
        print("Invalid rate:", test_rate)
    else:
        if is_rate_supported:
            print("Supported rate:", test_rate)
        else:
            print("Unsupported rate:", test_rate)
