import cv2
import math
import pprint
import numpy as np
path = r'C:\Users\admin\Desktop\PJAI.png' 
img = cv2.imread(path)

cv2.namedWindow('Image')
 
 
points = []
def get_points(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONUP:
        points.append((x, y))
        if len(points) == 2:
            cv2.destroyAllWindows()
cv2.setMouseCallback('Image', get_points)

while True:
    cv2.imshow('Image', img)
    if len(points) == 2:
        break
    cv2.waitKey(1)

print('Coordinate of point 1:', points[0])
print('Coordinate of point 2:', points[1])


A = [] #luu duong 2 chieu

path2 = r'C:\Users\admin\Desktop\2_chieu.txt' 
with open(path2, "r") as f:
      for line in f:
        a, b = map(int, line.strip().split('x'))
        A.append((a, b))


B = [] #luu duong 1 chieu

path3 = r'C:\Users\admin\Desktop\1_chieu.txt' 
with open(path3, "r") as f:
      for line in f:
        c, d = map(int, line.strip().split('x'))
        B.append((c, d))

#mang luu toa do cac duong

M = [] #diem giao
N = []
P = [] #1.1
Q = [] #1.2
C = [] #1.3
D = [] #1.4
R = [] #1.5
O = [] #1.6
E = [] #2.2
F = [] #2.3
G = [] #2.4
H = [] #2.5
I = [] #2.6
J = [] #2.7
K = [] #2.8
L = [] #2.9

with open("1_chieu1.txt", "r") as file1, open("1_chieu2.txt", "r") as file2, open("1_chieu3.txt", "r") as file3,open("1_chieu4.txt", "r") as file4,open("1_chieu5.txt", "r") as f5,open("1_chieu6.txt", "r") as f6 :
    for line1 in file1:
        a, b = map(int, line1.strip().split('x'))
        P.append((a, b))
    for line2 in file2:
        c, d = map(int, line2.strip().split('x'))
        Q.append((c, d))
    for line3 in file3:
        e, f = map(int, line3.strip().split('x'))
        C.append((e, f))
    for line4 in file4:
        e1, f1 = map(int, line4.strip().split('x'))
        D.append((e1, f1))
    for line5 in f5:
        e2, f2 = map(int, line5.strip().split('x'))
        R.append((e2, f2))
    for line6 in f6:
        e3, f3 = map(int, line6.strip().split('x'))
        O.append((e3, f3))

with open('2_chieu2.txt', 'r') as file5, open('2_chieu3.txt', 'r') as file6, open('2_chieu4.txt', 'r') as file7, open('2_chieu5.txt', 'r') as file8, open('2_chieu6.txt', 'r') as file9, open('2_chieu7.txt', 'r') as file10, open('2_chieu8.txt', 'r') as file11,  open('2_chieu9.txt', 'r') as file12:
    for line5 in file5:
        a2, b2 = map(int, line5.strip().split('x'))
        E.append((a2, b2))
    for line6 in file6:
        a3, b3 = map(int, line6.strip().split('x'))
        F.append((a3, b3))
    for line7 in file7:
        a4, b4 = map(int, line7.strip().split('x'))
        G.append((a4, b4))
    for line8 in file8:
        a5, b5 = map(int, line8.strip().split('x'))
        H.append((a5, b5))
    for line9 in file9:
        a6, b6 = map(int, line9.strip().split('x'))
        I.append((a6, b6))
    for line10 in file10:
        a7, b7 = map(int, line10.strip().split('x'))
        J.append((a7, b7))
    for line11 in file11:
        a8, b8 = map(int, line11.strip().split('x'))
        K.append((a8, b8))
    for line12 in file12:
        a9, b9 = map(int, line12.strip().split('x'))
        L.append((a9, b9))

with open('diem_giao.txt', 'r') as f:
    for l in f:
        a9, b9 = map(int, l.strip().split('x'))
        M.append((a9, b9))

def find_closest_point_by_j(x, arr): #tim diem giao gan nhat theo tung do
    closest_point = None
    min_distance = math.inf
    
    for point in arr:
        if point[0] <= x[0]:  # nếu tung do cua x  không lớn hơn tung do cua giao diem thì bỏ qua 
            continue
        distance = math.sqrt((point[0]-x[0])**2 + (point[1]-x[1])**2)  # tính khoảng cách Euclid
        if distance < min_distance:
            min_distance = distance
            closest_point = point
    return closest_point

def find_closest_point_by_j1(x, arr): #tim diem giao gan nhat theo tung do
    closest_point = None
    min_distance = math.inf
    
    for point in arr:
        if point[0] >= x[0]:  # nếu tung do cua x  không lớn hơn tung do cua giao diem thì bỏ qua 
            continue
        distance = math.sqrt((point[0]-x[0])**2 + (point[1]-x[1])**2)  # tính khoảng cách Euclid
        if distance < min_distance:
            min_distance = distance
            closest_point = point
    return closest_point

def find_closest_point_by_i(x, arr): #tim diem giao gan nhat theo hoanh do
    closest_point = None
    min_distance = math.inf
    
    for point in arr:
        if point[1] <= x[1]:  # nếu hoanh do cua x  không lớn hơn hoanh do cua giao diem thì bỏ qua 
            continue
        distance = math.sqrt((point[0]-x[0])**2 + (point[1]-x[1])**2)  # tính khoảng cách Euclid
        if distance < min_distance:
            min_distance = distance
            closest_point = point
    return closest_point

def find_closest_point_by_i1(x, arr): #tim diem giao gan nhat theo hoanh do
    closest_point = None
    min_distance = math.inf
    
    for point in arr:
        if point[1] >= x[1]:  # nếu hoanh do cua x  không lớn hơn hoanh do cua giao diem thì bỏ qua 
            continue
        distance = math.sqrt((point[0]-x[0])**2 + (point[1]-x[1])**2)  # tính khoảng cách Euclid
        if distance < min_distance:
            min_distance = distance
            closest_point = point
    return closest_point
#xet points[0]
closest_point_in_A = min(A, key=lambda x: math.sqrt((x[0]-points[0][0])**2 + (x[1]-points[0][1])**2))

# Tính khoảng cách Euclid giữa từng điểm trong mảng B với điểm points[0]
closest_point_in_B = min(B, key=lambda y: math.sqrt((y[0]-points[0][0])**2 + (y[1]-points[0][1])**2))

# So sánh khoảng cách Euclid và in ra kết quả tương ứng
distance_to_A = math.sqrt((closest_point_in_A[0]-points[0][0])**2 + (closest_point_in_A[1]-points[0][1])**2)
distance_to_B = math.sqrt((closest_point_in_B[0]-points[0][0])**2 + (closest_point_in_B[1]-points[0][1])**2)

if distance_to_A < distance_to_B:
    x = closest_point_in_A
    if x in E:
        common_elements = []
        for element in E:
            if element in M:
                common_elements.append(element)
        closest_point_x = min(common_elements, key=lambda m: math.sqrt((m[0]-x[0])**2 + (m[1]-x[1])**2))
        print(closest_point_x)
    elif x in F:
        common_elements = []
        for element in F:
            if element in M:
                common_elements.append(element)
        closest_point_x = min(common_elements, key=lambda m: math.sqrt((m[0]-x[0])**2 + (m[1]-x[1])**2))
        print(closest_point_x)
    elif x in G:
        common_elements = []
        for element in G:
            if element in M:
                common_elements.append(element)
        closest_point_x = min(common_elements, key=lambda m: math.sqrt((m[0]-x[0])**2 + (m[1]-x[1])**2))
        print(closest_point_x)
    elif x in H:
        common_elements = []
        for element in H:
            if element in M:
                common_elements.append(element)
        closest_point_x = min(common_elements, key=lambda m: math.sqrt((m[0]-x[0])**2 + (m[1]-x[1])**2))
        print(closest_point_x)
    elif x in I:
        common_elements = []
        for element in I:
            if element in M:
                common_elements.append(element)
        closest_point_x = min(common_elements, key=lambda m: math.sqrt((m[0]-x[0])**2 + (m[1]-x[1])**2))
        print(closest_point_x)
    elif x in J:
        common_elements = []
        for element in J:
            if element in M:
                common_elements.append(element)
        closest_point_x = min(common_elements, key=lambda m: math.sqrt((m[0]-x[0])**2 + (m[1]-x[1])**2))
        print(closest_point_x)
    elif x in K:
        common_elements = []
        for element in K:
            if element in M:
                common_elements.append(element)
        closest_point_x = min(common_elements, key=lambda m: math.sqrt((m[0]-x[0])**2 + (m[1]-x[1])**2))
        print(closest_point_x)
    elif x in L:
        common_elements = []
        for element in L:
            if element in M:
                common_elements.append(element)
        closest_point_x = min(common_elements, key=lambda m: math.sqrt((m[0]-x[0])**2 + (m[1]-x[1])**2))
        print(closest_point_x)
else:
    print("point[0] thuoc duong 1 chieu:", closest_point_in_B)
    x = closest_point_in_B
    if x in P:
        print("x thuoc duong 1_chieu1")
        common_elements = []
        for element in P:
            if element in M:
                common_elements.append(element)
        closest_point_x = find_closest_point_by_j(x, common_elements)
        print(closest_point_x)
    elif x in Q:
        print("x thuoc duong 1_chieu2")
        common_elements = []
        for element in Q:
            if element in M:
                common_elements.append(element)
        closest_point_x = find_closest_point_by_i(x, common_elements)
        print(closest_point_x)
    elif x in C:
        print("x thuoc duong 1_chieu3")
        common_elements = []
        for element in C:
            if element in M:
                common_elements.append(element)
        closest_point_x = find_closest_point_by_i(x, common_elements)
        print(closest_point_x)
    elif x in D:
        print("x thuoc duong 1_chieu4")
        common_elements = []
        for element in D:
            if element in M:
                common_elements.append(element)
        closest_point_x = find_closest_point_by_i(x, common_elements)
        print(closest_point_x)
    elif x in R:
        print("x thuoc duong 1_chieu5")
        common_elements = []
        for element in R:
            if element in M:
                common_elements.append(element)
        closest_point_x = find_closest_point_by_i1(x, common_elements)
        print(closest_point_x)
    elif x in O:
        print("x thuoc duong 1_chieu6")
        common_elements = []
        for element in O:
            if element in M:
                common_elements.append(element)
        closest_point_x = find_closest_point_by_i1(x, common_elements)
        print(closest_point_x)

#xet points[1]
closest_point_in_A1 = min(A, key=lambda z: math.sqrt((z[0]-points[1][0])**2 + (z[1]-points[1][1])**2))

# Tính khoảng cách Euclid giữa từng điểm trong mảng B với điểm points[0]
closest_point_in_B1 = min(B, key=lambda k: math.sqrt((k[0]-points[1][0])**2 + (k[1]-points[1][1])**2))

# So sánh khoảng cách Euclid và in ra kết quả tương ứng
distance_to_A1 = math.sqrt((closest_point_in_A1[0]-points[1][0])**2 + (closest_point_in_A1[1]-points[1][1])**2)
distance_to_B1 = math.sqrt((closest_point_in_B1[0]-points[1][0])**2 + (closest_point_in_B1[1]-points[1][1])**2)

if distance_to_A1 < distance_to_B1:
    print("point[1] thuoc duong 2 chieu:", closest_point_in_A1)
    y = closest_point_in_A1
    if y in E:
        print("y thuoc duong 2_chieu2")
        common_elements = []
        for element in E:
            if element in M:
                common_elements.append(element)
        closest_point_y = min(common_elements, key=lambda m: math.sqrt((m[0]-y[0])**2 + (m[1]-y[1])**2))
        print(closest_point_y)
    elif y in F:
        print("y thuoc duong 2_chieu3")
        common_elements = []
        for element in F:
            if element in M:
                common_elements.append(element)
        closest_point_y = min(common_elements, key=lambda m: math.sqrt((m[0]-y[0])**2 + (m[1]-y[1])**2))
        print(closest_point_y)
    elif y in G:
        print("y thuoc duong 2_chieu4")
        common_elements = []
        for element in G:
            if element in M:
                common_elements.append(element)
        closest_point_y = min(common_elements, key=lambda m: math.sqrt((m[0]-y[0])**2 + (m[1]-y[1])**2))
        print(closest_point_y)
    elif y in H:
        print("y thuoc duong 2_chieu5")
        common_elements = []
        for element in H:
            if element in M:
                common_elements.append(element)
        closest_point_y = min(common_elements, key=lambda m: math.sqrt((m[0]-y[0])**2 + (m[1]-y[1])**2))
        print(closest_point_y)
    elif y in I:
        print("y thuoc duong 2_chieu6")
        common_elements = []
        for element in I:
            if element in M:
                common_elements.append(element)
        closest_point_y = min(common_elements, key=lambda m: math.sqrt((m[0]-y[0])**2 + (m[1]-y[1])**2))
        print(closest_point_y)
    elif y in J:
        print("y thuoc duong 2_chieu7")
        common_elements = []
        for element in J:
            if element in M:
                common_elements.append(element)
        closest_point_y = min(common_elements, key=lambda m: math.sqrt((m[0]-y[0])**2 + (m[1]-y[1])**2))
        print(closest_point_y)
    elif y in K:
        print("y thuoc duong 2_chieu8")
        common_elements = []
        for element in K:
            if element in M:
                common_elements.append(element)
        closest_point_y = min(common_elements, key=lambda m: math.sqrt((m[0]-y[0])**2 + (m[1]-y[1])**2))
        print(closest_point_y)
    elif y in L:
        common_elements = []
        for element in L:
            if element in M:
                common_elements.append(element)
        closest_point_y = min(common_elements, key=lambda m: math.sqrt((m[0]-y[0])**2 + (m[1]-y[1])**2))
        print(closest_point_y)
else:
    print("point[1] thuoc duong 1 chieu:", closest_point_in_B1)
    y = closest_point_in_B1
    if y in P:
        print("y thuoc duong 1_chieu1")
        common_elements = []
        for element in P:
            if element in M:
                common_elements.append(element)
        closest_point_y = find_closest_point_by_j1(y, common_elements)
        print(closest_point_y)
        if x in P:
            closest_point_y1 = find_closest_point_by_j(y, common_elements)
            print(closest_point_y1)
            if closest_point_x == closest_point_y1:
                if points[0][0] < points[1][0]:
                    cv2.line(img, points[0], points[1], color=(0,0, 255), thickness=2)
                    cv2.imshow('Image', img)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
                    exit()
        

    elif y in Q:
        print("y thuoc duong 1_chieu2")
        common_elements = []
        for element in Q:
            if element in M:
                common_elements.append(element)
        closest_point_y = find_closest_point_by_i1(y, common_elements)
        print(closest_point_y)
        if x in Q:
            closest_point_y1 = find_closest_point_by_i(y, common_elements)
            print(closest_point_y1)
            if closest_point_x == closest_point_y1:
                if points[0][1] < points[1][1]:
                    cv2.line(img, points[0], points[1], color=(0,0, 255), thickness=2)
                    cv2.imshow('Image', img)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
                    exit()
    elif y in C:
        print("y thuoc duong 1_chieu3")
        common_elements = []
        for element in C:
            if element in M:
                common_elements.append(element)
        closest_point_y = find_closest_point_by_i1(y, common_elements)
        print(closest_point_y)
        if x in C:
            closest_point_y1 = find_closest_point_by_i(y, common_elements)
            print(closest_point_y1)
            if closest_point_x == closest_point_y1:
                if points[0][1] < points[1][1]:
                    cv2.line(img, points[0], points[1], color=(0,0, 255), thickness=2)
                    cv2.imshow('Image', img)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
                    exit()
    elif y in D:
        print("y thuoc duong 1_chieu4")
        common_elements = []
        for element in D:
            if element in M:
                common_elements.append(element)
        closest_point_y = find_closest_point_by_j(y, common_elements)
        print(closest_point_y)
        if x in D:
            closest_point_y1 = find_closest_point_by_j1(y, common_elements)
            print(closest_point_y1)
            if closest_point_x == closest_point_y1:
                if points[0][1] < points[1][1]:
                    cv2.line(img, points[0], points[1], color=(0,0, 255), thickness=2)
                    cv2.imshow('Image', img)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
                    exit()
    elif y in R:
        print("y thuoc duong 1_chieu5")
        common_elements = []
        for element in R:
            if element in M:
                common_elements.append(element)
        closest_point_y = find_closest_point_by_i(y, common_elements)
        print(closest_point_x)
        if x in R:
            closest_point_y1 = find_closest_point_by_i1(y, common_elements)
            print(closest_point_y1)
            if closest_point_x == closest_point_y1:
                if points[0][0] < points[1][0]:
                    cv2.line(img, points[0], points[1], color=(0,0, 255), thickness=2)
                    cv2.imshow('Image', img)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
                    exit()
    elif y in O:
        print("y thuoc duong 1_chieu6")
        common_elements = []
        for element in O:
            if element in M:
                common_elements.append(element)
        closest_point_y = find_closest_point_by_j(y, common_elements)
        print(closest_point_y)
        if x in O:
            closest_point_y1 = find_closest_point_by_j1(y, common_elements)
            print(closest_point_y1)
            if closest_point_x == closest_point_y1:
                if points[0][1] > points[1][1]:
                    cv2.line(img, points[0], points[1], color=(0,0, 255), thickness=2)
                    cv2.imshow('Image', img)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
                    exit()
if closest_point_x == (254,131): #diem giao
    x = 'A'
elif closest_point_x == (344,149):
    x = 'B'
elif closest_point_x == (495,179):
    x = 'C'
elif closest_point_x == (495, 194):
    x = 'D'
elif closest_point_x == (367,261):
    x = 'E'
elif closest_point_x == (496,267):
    x = 'F'
elif closest_point_x == (370,277):
    x = 'G'
elif closest_point_x == (318,281):
    x = 'H'
elif closest_point_x == (289,433):
    x = 'I'
elif closest_point_x == (336, 437):
    x = 'J'
elif closest_point_x == (460, 487):
    x = 'K'
elif closest_point_x == (373, 523):
    x = 'L'
elif closest_point_x == (263, 567):
    x = 'M'
elif closest_point_x == (493, 561):
    x = 'N'
elif closest_point_x == (462, 577):
    x = 'O'
elif closest_point_x == (408, 606):
    x = 'P'
elif closest_point_x == (240, 687):
    x = 'Q'
elif closest_point_x == (230, 735):
    x = 'R'
elif closest_point_x == (134, 712):
    x = 'S'

if closest_point_y == (254,131): 
    y = 'A'
elif closest_point_y == (344,149):
    y = 'B'
elif closest_point_y == (495,179):
   y = 'C'
elif closest_point_y == (495, 194):
    y= 'D'
elif closest_point_y == (366,262):
    y = 'E'
elif closest_point_y == (496,267):
    y = 'F'
elif closest_point_y == (370,277):
    y = 'G'
elif closest_point_y == (318,281):
    y = 'H'
elif closest_point_y == (289,433):
    y = 'I'
elif closest_point_y == (336, 437):
    y = 'J'
elif closest_point_y == (460, 487):
    y = 'K'
elif closest_point_y == (373, 523):
    y = 'L'
elif closest_point_y == (263, 567):
    y = 'M'
elif closest_point_y == (493, 561):
    y = 'N'
elif closest_point_y == (462, 577):
    y = 'O'
elif closest_point_y == (408, 606):
    y = 'P'
elif closest_point_y == (240, 687):
    y = 'Q'
elif closest_point_y == (230, 735):
    y = 'R'
elif closest_point_y == (134, 712):
    y = 'S'

class Dijkstra:
    def __init__(self, graph, start_vertex):
        self.graph = graph
        self.start_vertex = start_vertex
        self.vertices = list(graph.keys())

        # distance: minimum distance from start vertex
        self.vertex_labels = {vertex: {'distance': math.inf, 'prev': '-'} for vertex in self.vertices}

        # Obviously, the start vertex has no distance from itself
        self.vertex_labels[start_vertex]['distance'] = 0


    def _get_edge_weight(self, vertex1, vertex2):
        try:
            return self.graph[vertex1][vertex2]
        except KeyError:
            return math.inf


    def _set_label(self, vertex, weight, prev=''):
        self.vertex_labels[vertex]['distance'] = weight

        if prev:
            self.vertex_labels[vertex]['prev'] = prev


    def _get_label(self, vertex):
        return self.vertex_labels[vertex]


    def dijkstra(self):
        interiors = [self.start_vertex]
        max_interior_vertices = len(self.vertices)

        while True:
            exteriors = [vertex for vertex in self.vertices if vertex not in interiors]

            # Nearest vertex to start vertex
            nearest_vertex = '-'

            # Distance from start index
            nearest_vertex_distance = math.inf

            for exterior in exteriors:
                exterior_label = self._get_label(exterior)

                # Shortest discovered distance of current outerior from start vertex
                shortest_discovered_distance = exterior_label['distance']

                # Last vertex through which we reached current exterior with shortest distance
                choosen_prev = exterior_label['prev']

                for interior in interiors:
                    # Shortest discovered distance of current interior from start vertex + distance of current interior from current exterior
                    distance_from_exterior = self._get_label(interior)['distance'] + self._get_edge_weight(interior, exterior)

                    if distance_from_exterior < shortest_discovered_distance:
                        shortest_discovered_distance = distance_from_exterior
                        choosen_prev = interior
            
                self._set_label(exterior, shortest_discovered_distance, choosen_prev)

                # Attempt to find the nearest exterior to start vertex
                if shortest_discovered_distance < nearest_vertex_distance:
                    nearest_vertex_distance = shortest_discovered_distance
                    nearest_vertex = exterior
            
            interiors.append(nearest_vertex)

            if len(interiors) == max_interior_vertices:
                break


    def build_path(self, vertex):
        if vertex == '-':
            return []
        
        return self.build_path(self.vertex_labels[vertex]['prev']) + [vertex]


graph = {'A': {'B': 91.78,'S': 593.26},
         'B': {'A': 91.78, 'C': 153.95},
         'C': {'B': 153.95, 'D': 15},
         'D': {'C': 15, 'E': 145.83, 'F': 73.01},
         'E': {'B': 115.12, 'D': 145.83},
         'F': {'D': 73.01, 'G': 126.4, 'K': 222.93},
         'G' : {'E': 15.52, 'H' : 52.15, 'K': 228.47},
         'H' : {'B': 134.54},
         'K': {'F': 222.93, 'G': 228.47, 'L' : 94.15, 'O': 90.02, 'N': 81.02},
         'L': {'J': 93.62, 'M': 118.47, 'P': 90.08},
         'M': {'I': 136.5},
         'I': {'H': 154.74, 'J': 47.17},
         'J': {'I': 47.17, 'L': 93.62},
         'N': {'K': 81.02, 'O': 34.89},
         'O': {'N': 34.89, 'K': 90.02},
         'P': {'L': 90.08, 'O': 61.29},
         'Q': {'M': 122.18, 'P': 186.51},
         'R': {'Q': 49.03, 'S': 98.72},
         'S': {'R': 98.72}
         }

dijkstra = Dijkstra(graph, start_vertex= x)

# Run the algorithm
dijkstra.dijkstra()
Dijk = dijkstra.build_path(y)
print(x, '->' ,y,':', Dijk)


Arr = [(254,131), (344,149),(495,179), (495, 194), (367,261), (496,267), (370,277),(318,281), (289,433),
       (336, 437), (460, 487),(373, 523),(263, 567), (493, 561),(462, 577), (408, 606), (240,687), (230,735), (134,712) ]
arr = ['A', 'B', 'C', 'D', 'E', 'F','G','H', 'I', 'J','K', 'L', 'M', 'N','O', 'P', 'Q', 'R', 'S']
dict_mapping = {}
for i in range(len(Arr)):
    dict_mapping[arr[i]] = Arr[i]
print(dict_mapping)
result = []


for i in Dijk:
    # Kiểm tra nếu phần tử có trong cả hai mảng
    if i in dict_mapping:
        result.append(dict_mapping[i])

arr_list = [E,F,G,H,I,J,K, L]
Arr_list = [P,Q,C, D, R, O]
#hien thi len anh
if distance_to_A < distance_to_B: #diem 1 nam tren duong 2 chieu
    result.insert(0, points[0])
    result.insert(1,closest_point_in_A)
    print(result)
    if result[2][0] <= points[0][0] <= result[3][0] and result[2][1] <= points[0][1] <= result[3][1]:
        del result[2]
        print('a')
    elif result[2][0] >= points[0][0] >= result[3][0] and result[2][1] <= points[0][1] <= result[3][1]:
        del result[2]
        print('m')
    if distance_to_A1 < distance_to_B1 : #diem 2 nam tren duong 2 chieu
        for arr in arr_list:
            if closest_point_in_A1 in arr and closest_point_in_A in arr: #tren cung 1 duong
                cv2.line(img, points[0], points[1], color=(0, 0, 255), thickness=2)
                cv2.circle(img, points[0],radius=0, color=(0, 0, 255), thickness=10)
                cv2.circle(img, points[1],radius=0, color=(0, 255, 0), thickness=10)
                cv2.imshow('Image', img)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                exit()
        else: #2 duong khac nhau
                result.append(closest_point_in_A1)
                result.append(points[1])
                i = len(result)
                print(i)
                p = np.array(result)
                print(result)
                for arr in arr_list:
                    if result[i-3] in arr and result[i-4] in arr and closest_point_in_A1 in arr:
                        del result[i-3]
                        p = np.array(result)
                        cv2.polylines(img, [p], isClosed=False, color=(0,0, 255), thickness=2)
                        cv2.circle(img, points[0],radius=0, color=(0, 0, 255), thickness=10)
                        cv2.circle(img, points[1],radius=0, color=(0, 255, 0), thickness=10)
                        cv2.imshow('Image', img)
                        cv2.waitKey(0)
                        cv2.destroyAllWindows()
                        exit()
                    
                else:
                    cv2.polylines(img, [p], isClosed=False, color=(0,0, 255), thickness=2)
                    cv2.circle(img, points[0],radius=0, color=(0, 0, 255), thickness=10)
                    cv2.circle(img, points[1],radius=0, color=(0, 255, 0), thickness=10)
                    cv2.imshow('Image', img)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()

    else: #diem 2 nam tren duong 1 chieu
            result.append(closest_point_in_B1)
            print('c')
            result.append(points[1])
            p = np.array(result)
            print(result)
            cv2.polylines(img, [p], isClosed=False, color=(0,0, 255), thickness=2)
            cv2.circle(img, points[0],radius=0, color=(0, 0, 255), thickness=10)
            cv2.circle(img, points[1],radius=0, color=(0, 255, 0), thickness=10)
            cv2.imshow('Image', img)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
else: #diem 1 thuoc duong 1 chieu
    result.insert(0, points[0])
    result.insert(1,closest_point_in_B)
    if distance_to_A1 < distance_to_B1: #diem 2 thuoc duong 2 chieu
        result.append(closest_point_in_A1)
        result.append(points[1])
        p = np.array(result)
        print(result)
        i = len(result)
        print(i)
        for arr in arr_list:
            if result[i-3] in arr and result[i-4] in arr and closest_point_in_A1 in arr:
                    del result[i-3]
                    print(result)
                    p = np.array(result)
                    cv2.polylines(img, [p], isClosed=False, color=(0,0, 255), thickness=2)
                    cv2.circle(img, points[0],radius=0, color=(0, 0, 255), thickness=10)
                    cv2.circle(img, points[1],radius=0, color=(0, 255, 0), thickness=10)
                    cv2.imshow('Image', img)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
                    exit()
            else:
                    cv2.polylines(img, [p], isClosed=False, color=(0,0, 255), thickness=2)
                    cv2.circle(img, points[0],radius=0, color=(0, 0, 255), thickness=10)
                    cv2.circle(img, points[1],radius=0, color=(0, 255, 0), thickness=10)
                    cv2.imshow('Image', img)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
                    exit()
            
            
    else: #diem 2 thuoc duong 1 chieu
        for arr in Arr_list:
            if closest_point_in_B1 in arr and closest_point_in_B in arr: #tren cung 1 duong
                
                if closest_point_x != closest_point_y:
                    result.append(closest_point_in_B1)
                    result.append(points[1])
                    p = np.array(result)
                    print(result)
                    cv2.polylines(img, [p], isClosed=False, color=(0,0, 255), thickness=2)
                    cv2.circle(img, points[0],radius=0, color=(0, 0, 255), thickness=10)
                    cv2.circle(img, points[1],radius=0, color=(0, 255, 0), thickness=10)
                    cv2.imshow('Image', img)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
                    exit()

        else: #2 duong khac nhau
                    result.append(closest_point_in_B1)
                    result.append(points[1])
                    p = np.array(result)
                    print(result)
                    cv2.polylines(img, [p], isClosed=False, color=(0,0, 255), thickness=2)
                    cv2.circle(img, points[0],radius=0, color=(0, 0, 255), thickness=10)
                    cv2.circle(img, points[1],radius=0, color=(0, 255, 0), thickness=10)
                    cv2.imshow('Image', img)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
