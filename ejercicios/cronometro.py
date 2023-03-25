  
#-----------------------------------------------------------
#             main()
#-----------------------------------------------------------

def main():
    print("Hello World!")
    # This entrypoint file to be used in development. Start by reading README.md
    from cronometro_time import add_time

    print(f'{add_time("3:00 PM", "3:10")}\n')
    print(f'{add_time("11:06 PM", "2:02")}\n')
    print(f'{add_time("11:43 AM", "00:20")}\n')
    print(f'{add_time("10:10 PM", "3:30")}\n')
    print(f'{add_time("6:30 PM", "205:12")}\n')


    print(f'{add_time("11:30 AM", "2:32", "Monday")}\n')
    print(f'{add_time("11:43 PM", "24:20", "tueSday")}\n')
    


if __name__ == "__main__":
    main()
    
    
#------------------------------
# Hello World!
# Dias=0 Hrs=18  Min=10
# 06:10 PM
# 
# Dias=1 Hrs=1  Min=8
# 01:08 AM ( next day )
# 
# Dias=0 Hrs=12  Min=3
# 12:03 AM
# 
# Dias=1 Hrs=1  Min=40
# 01:40 AM ( next day )
# 
# Dias=9 Hrs=7  Min=42
# 07:42 AM ( 9 day later )
# 
# Dias=0 Hrs=14  Min=2
# 02:02 PM, monday
# 
# Dias=2 Hrs=12  Min=3
# 12:03 AM, thursday ( 2 day later )    
# 