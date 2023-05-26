import csv


class Track:

    def __init__(self):
        self.car_position = {}  # key car obj, value int pos in list of segments
        self.track_segments = []
        self.name = ""
        self.total_length = 0
        self.current_segment = None

    def add_track_segment(self, segment):
        self.track_segments.append(segment)

        if self.current_segment is None:
            self.current_segment = self.track_segments[0]


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


def get_segment(lst):
    segment_list = []
    for row in lst:
        if row[1] == "Straight":
            segment = Straight(float(row[3]) * 1000, 0, 0)
        elif row[1] == "Corner":
            segment = Corner(0, 0, float(row[3]) * 1000, row[2])
        else:

            raise ValueError("Unknown segment type: " + row[1])

        segment_list.append(segment)

    return segment_list


def create_track(CSV_file, name):
    test = Track()
    test.name = name
    for segment in get_segment(create_seg_list(CSV_file)):
        test.add_track_segment(segment)
        test.total_length += segment.length

    return test
