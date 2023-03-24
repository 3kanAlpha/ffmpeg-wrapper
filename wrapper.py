import os, sys, subprocess, glob

VIDEO_EXT = ['mp4', 'avi', 'mov']
AUDIO_EXT = ['mp3', 'wav']

def check_if_path_is_video(path):
    ext = os.path.splitext(path)[1][1:].lower()
    return ext in VIDEO_EXT

def check_if_path_is_audio(path):
    ext = os.path.splitext(path)[1][1:].lower()
    return ext in AUDIO_EXT

def escape_filename(filename: str):
    filename.replace(r'⧸', '_')
    return filename

def split_video(path, l_sec):
    input_dir = os.path.dirname(path)
    # path = escape_filename(path)
    basename = os.path.basename(path)
    # print(basename)
    # basename = escape_filename(basename)
    root, ext = os.path.splitext(basename)
    output_dir = os.path.join(input_dir, root)
    
    if not os.path.exists(output_dir):
        # OSError WinError 123
        os.makedirs(output_dir)
    
    output_filename = os.path.join(output_dir, '%03d' + ext)
    
    cp = subprocess.run(['ffmpeg', '-i', path, '-c', 'copy', '-map', '0', '-segment_time', str(l_sec), '-f', 'segment', '-reset_timestamps', '1', output_filename])

def run_wrapper():
    args = sys.argv[1:]
    
    if len(args) < 1:
        print('No arguments provided')
        sys.exit(1)
    
    cmd_type = args[0].lower()
    # print(args)
    
    if cmd_type == 'split':
        input_filepath = args[1]
        split_interval = args[2]
        
        split_interval_sec = -1
        if split_interval[-1] == 'm':
            split_interval_sec = int(split_interval[:-1]) * 60
        elif split_interval[-1] == 's':
            split_interval_sec = int(split_interval[:-1])
        else:
            split_interval_sec = int(split_interval)
        
        if check_if_path_is_video(input_filepath):
            split_video(input_filepath, split_interval_sec)
    
def main():
    run_wrapper()

if __name__ == '__main__':
    main()