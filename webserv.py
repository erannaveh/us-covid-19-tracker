from flask import Flask

app = Flask(__name__)

"""
API List:
    1. Graph Selected States By Cases/Deaths X
    2. Graph Selected Counties By Cases/Deaths
    3. Top N States By Cases/Death
    4. Top N Counties Nationally/State By Cases/Death
    5. Table for Selected States
    6. Table for Selected Counties
"""

@app.route("/states/graph/selected/<stateList>/<deathsOrCases>")
def statesGraph(stateList, deathsOrCases):

    return "This will return graph for "+stateList+" "+deathsOrCases

@app.route("/counties/graph/selected/<countiesList>/<deathsOrCases>")
def countiesGraph(countiesList, deathsOrCases):
    return "This will return graph for "+countiesList+" "+deathsOrCases

@app.route("/states/table/topn/<numStates>/<deathsOrCases>")
def topNStates(numStates, deathsOrCases):
    return "This will return table for top "+numStates+" "+deathsOrCases

@app.route("/counties/table/topn/<numCounties>/<deathsOrCases>/<state>")
def topNCounties(numCounties, deathsOrCases, state='empty'):
    return "This will return table for top "+numCounties+" "+deathsOrCases+" either nationally or of specific state"

@app.route("/states/table/selected/<stateList>")
def statesTable(stateList):
    return " <!DOCTYPE html><html><body><b> This will return table for "+stateList+"</b></body></html>"

@app.route("/counties/table/selected/<countiesList>")
def countiesTable(countiesList):
    return "This will return table for "+countiesList

#default landing page
@app.route("/")
def hello():
    return """
        <!DOCTYPE html>
        <head>
        <title>My title</title>
        <link rel="stylesheet" href="http://stash.compjour.org/assets/css/foundation.css">
         <script>
            function loadif1() {
                if1=document.getElementById("if1");
                if1.src="/counties/table/selected/a,b,c";
            }
        </script>
        </head>
        <body style="width: 880px; margin: auto;">  
           <h1>Visible stuff goes here</h1>
            <p>here's a paragraph, fwiw</p>
            <p>And here's an image:</p>
            <a href="https://www.flickr.com/photos/zokuga/14615349406/">
                <img src="http://stash.compjour.org/assets/images/sunset.jpg" alt="it's a nice sunset">
            </a>
            <br>
            <button align=center type=button onclick="loadif1()">Click me</button><br>
            <iframe border=0 src='' id=if1 name=if1 align=center width='50%' height='25%'>
            </iframe>
        </body>
        """


if __name__ == "__main__":
    app.run()