def image_processor():
    function_dict = { '1': show_an_image,
                      '2': mirror_image,
                      '3': put_behind_bar,
                      '4': put_behind_bar_transparent,
                      '5': circle_pic,
                      '6': blur_image,
                      '7': rotate_image,
                      'Q': exit}
    print('Welcome to IT1007 Image Processor')
    filename = input('Please enter the file name: ')
    print('Filename =',filename)
    print('Please select an operation you want to perform')
    print('1. Show the image')
    print('2. Mirror image')
    print('3. Put behind bar')
    print('4. Put behind transparent bar')
    print('5. Circle Picture')
    print('6. Blurring')
    print('7. Rotation')
    print('Q. Quit')
    while True:
        choice = input('Enter your choice (1-7,Q): ')
        if choice in function_dict.keys():
            function_dict[choice](filename)
            continue
        else:
            print('Invalid choice!')
            continue
    return    
