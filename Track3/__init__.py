import csv


class Track:

    def __init__(self):
        self.car_position = {}  # key car obj, value int pos in list of segments
        self.track_segments = []
        self.name = ""
        self.total_length = 0

    def add_track_segment(self, segment):
        self.track_segments.append(segment)


class Corner:
    def __init__(self, difficulty, overtakeDifficulty, length, direction):
        self.difficulty = float(difficulty)
        self.overtakeDifficulty = float(overtakeDifficulty)
        self.length = float(length)
        self.direction = str(direction)


class Straight:
    def __init__(self, length, brakingDifficulty, overtakeBrakingDifficulty):
        self.length = float(length)
        self.brakingDifficulty = float(brakingDifficulty)
        self.overtakeBrakingDifficulty = float(overtakeBrakingDifficulty)


def create_seg_list(file):
    seg_list = []
    with open(file, "r") as f:
        reader = csv.reader(f)
        for row in reader:
            seg_list.append(row)

    return seg_list


def get_segment(list):
    l1 = list
    l2 = []
    x = 0
    y = 0
    while y < len(l1):
        for i in l1:
            if l1[x][1] == "Straight":
                segment = Straight(l1[x][3], 0, 0)
                x += 1
                y += 1
                l2.append(segment)

            elif l1[x][1] == "Corner":
                segment = Corner(0, 0, l1[x][3], l1[x][2])
                x += 1
                y += 1
                l2.append(segment)
            # add else - error message

    return l2


# trackSeg = create_seg_list("Silverstone.csv")
#
# # print(trackSeg)
# # print(get_segment(trackSeg))
#
# test = Track()
#
# for segment in get_segment(trackSeg):
#     test.add_track_segment(segment)
#
# # print(test.track_segments[11])
# print(test)


def create_track(CSV_file, name):
    test = Track()
    test.name = name
    for segment in get_segment(create_seg_list(CSV_file)):
        test.add_track_segment(segment)
        test.total_length += segment.length
    test.total_length = test.total_length * 1000

    return test






