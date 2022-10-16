from flask import Flask, render_template, request, url_for, redirect
from dij import Graph

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index(): 

    if request.method == 'POST':
        startPoint = int(request.form['startPoint']);
        endPoint = int(request.form['endPoint']);
        
        return  g.dijkstra(startPoint, endPoint)

    else:
            return render_template('main.html')

############

if __name__ == "__main__":
    # edges = Graph(54)
    # edges = {
    #     0: {1:1.5, 25:3},
    #     1: {2:3.5, 3:5, 25:1.5, 26:7},
    #     3: {2:2, 4:1.5, 5:3, 7:5, 6:4},
    #     7: {5:2, 6:1, 3:5, 4:5.3, 8:2.5, 9:3, 10:5.5, 11:6},
    #     10: {8:3.5, 9:2, 11:1.5, 12:1.5, 13:6, 14:8, 15:7},
    #     14: {13:2, 12:7, 15:1.8, 16:1.5, 17:4, 33:6, 34:7},
    #     15: {12:7, 13:3, 18:1, 19:2.5, 20:3, 21:4},
    #     21: {18:3, 19:2, 20:1, 22:1.5, 23:3, 24:3, 25:4},
    #     25: {23:1.5, 26:6},
    #     26: {27:1.5, 48:7},
    #     27: {28:2.5, 29:4, 30:4.5, 48:6},
    #     29: {28:2.5, 30:1, 31:2.5, 32:4},
    #     32: {30:4.5, 31:2, 33:1.5, 35:5.5, 36:8.5, 38:10},
    #     33: {16:5, 17:2.5, 34:1.5, 35:4, 36:8, 37:6.5},
    #     37: {35:3, 36:3, 38:3, 43:2.5, 44:4, 45:4.5},
    #     38: {35:6, 36:2, 39:3.5, 40:7, 41:5 , 42:2},
    #     44: {43:2.5, 45:1.5, 46:2, 47:4},
    #     47: {46:2, 45:4.5, 48:1.5, 53:3, 49:4},
    #     48: {26:4, 53:2.5, 49:5}, 
    #     49: {53:2.5, 50:3.5, 52:3.5, 51:7}
    # }
    g = Graph(54)
    g.add_edge(0,1,1.5)
    g.add_edge(0,25,3)
    g.add_edge(0,26,6)
    

    g.add_edge(1,2,3.5)
    g.add_edge(1,3,5)
    g.add_edge(1,25,1.5)
    g.add_edge(1,26,7)

    g.add_edge(3,2,2)
    g.add_edge(3,4,1.5)
    g.add_edge(3,5,3)
    g.add_edge(3,7,5)
    g.add_edge(3,6,4)

    g.add_edge(7,5,2)
    g.add_edge(7,6,1)
    g.add_edge(7,3,5)
    g.add_edge(7,4,5.3)
    g.add_edge(7,8,2.5)
    g.add_edge(7,9,3)
    g.add_edge(7,10,5.5)
    g.add_edge(7,11,6)

    g.add_edge(10,8,3.5)
    g.add_edge(10,9,2)
    g.add_edge(10,11,1.5)
    g.add_edge(10,12,1.5)
    g.add_edge(10,13,6)
    g.add_edge(10,14,8)
    g.add_edge(10,15,7)

    g.add_edge(14,13,2)
    g.add_edge(14,12,7)
    g.add_edge(14,15,1.8)
    g.add_edge(14,16,1.5)
    g.add_edge(14,17,4)
    g.add_edge(14,33,6)
    g.add_edge(14,34,7)

    g.add_edge(15,12,7)
    g.add_edge(15,13,3)
    g.add_edge(15,18,1)
    g.add_edge(15,19,2.5)
    g.add_edge(15,20,3)
    g.add_edge(15,21,4)

    g.add_edge(21,18,3)
    g.add_edge(21,19,2)
    g.add_edge(21,20,1)
    g.add_edge(21,22,1.5)
    g.add_edge(21,23,3)
    g.add_edge(21,24,3)
    g.add_edge(21,25,4)

    g.add_edge(25,23,1.5)
    g.add_edge(25,26,6)

    g.add_edge(26,27,1.5)
    g.add_edge(26,48,7)

    g.add_edge(27,28,2.5)
    g.add_edge(27,29,4)
    g.add_edge(27,30,4.5)
    g.add_edge(27,48,6)

    g.add_edge(29,28,2.5)
    g.add_edge(29,30,1)
    g.add_edge(29,31,2.5)
    g.add_edge(29,32,4)

    g.add_edge(32,30,4.5)
    g.add_edge(32,31,2)
    g.add_edge(32,33,1.5)
    g.add_edge(32,35,5.5)
    g.add_edge(32,36,8.5)
    g.add_edge(32,38,10)

    g.add_edge(33,16,5)
    g.add_edge(33,17,2.5)
    g.add_edge(33,34,1.5)
    g.add_edge(33,35,4)
    g.add_edge(33,36,8)
    g.add_edge(33,37,6.5)

    g.add_edge(37,35,3)
    g.add_edge(37,36,3)
    g.add_edge(37,38,3)
    g.add_edge(37,43,2.5)
    g.add_edge(37,44,4)
    g.add_edge(37,45,4.5)

    g.add_edge(38,35,6)
    g.add_edge(38,36,2)
    g.add_edge(38,39,3.5)
    g.add_edge(38,40,7)
    g.add_edge(38,41,5)
    g.add_edge(38,42,2)

    g.add_edge(44,43,2.5)
    g.add_edge(44,45,1.5)
    g.add_edge(44,46,2)
    g.add_edge(44,47,4)

    g.add_edge(47,46,2)
    g.add_edge(47,45,4.5)
    g.add_edge(47,48,1.5)
    g.add_edge(47,53,3)
    g.add_edge(47,49,4)

    g.add_edge(48,26,4)
    g.add_edge(48,53,2.5)
    g.add_edge(48,49,5)

    g.add_edge(49,53,2.5)
    g.add_edge(49,50,3.5)
    g.add_edge(49,52,3.5)
    g.add_edge(49,51,7)

    app.run(debug=True)  
