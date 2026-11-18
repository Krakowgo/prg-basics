def time_strings(hours,minutes,time_format):
    st_hours = ''
    st_mins = ''

    if time_format == 24:
        st_hours = str(hours)
        st_mins = str(minutes)
    else:
        if hours == 12:
            st_mins = str(minutes) + 'pm'
            st_hours = str(hours)
        elif hours > 12:
            st_mins = str(minutes) + 'pm'
            st_hours = str(hours - 12)
        else:
            st_hours = str(hours)
            st_mins = str(minutes) + 'am'
    return st_hours, st_mins
print(time_strings(15,38,24))
print(time_strings(0,7,12))