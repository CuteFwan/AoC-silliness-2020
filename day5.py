my_table = 'FBLR'
your_table = '0101'
trans_table = str.maketrans(my_table, your_table)


with open('input5.txt') as f:
    not_my_boarding_passes = []
    for photo in f.read().split():
        better_photo = photo.translate(trans_table)
        not_my_boarding_passes.append([
            int(better_photo[:7],2),
            int(better_photo[7:],2),
            int(better_photo,2)])
def sanity_check(passes):
    return max(not_my_boarding_passes, key=lambda p: p[2])[2]

def find_my_seat_right_now_or_I_will_get_kicked_off_the_plane_and_cry(passes):
    ordered_pases = sorted(not_my_boarding_passes, key=lambda p: p[2])
    last = ordered_pases[0][2]
    for row, col, ID in ordered_pases[1:]:
        if ID - last == 2:
            return ID - 1
        last = ID
print(sanity_check(not_my_boarding_passes))
print(find_my_seat_right_now_or_I_will_get_kicked_off_the_plane_and_cry(not_my_boarding_passes))