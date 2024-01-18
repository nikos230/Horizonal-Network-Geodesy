# Horizontal Network Geodesy (2D)
A script to solve horizontalNetworks in Geodesy with Least Squers Method and Minimum External Constraints <br/><br/>
Input --> Horizontal Gons, Distances and names and values, Orientantion of Network<br/>
Output --> Corrected Point Coordinates in the Refenernce System input data is in, Plot Points in diagram (geometry of the network) and Report about the Quality of the Network such as Sigma 0 and more <br/><br/>
Νecessary librarys are NumPy, FPDF and MatPlotLib<br/>


---

# Features

- Solve Horizontal Netowrk given the Horizontal Gons and Distances of points in the netowrk
- Calculate Temporary Coords from above data
- Plot Final Points in diagram and see geometry of Network
- Output final points in .txt file
- Generate Report in PDF with all corrected points and it errors (from covariance matrix) and Residuals of every coordinate of every point, Sigma 0 and more
- Output PDF and image of netowork is in A4 size so its easy to print after


# Usage
This script can be utilized for Solving Horizontal Networks and Plot the Result Points and tweek parameters of the method such as sigma of distances and sigma of gons. However, it is not recommended for professional use due to bugs and its inability to work with all input data. Instead, it is better suited for research purposes.<br/><br/>
Import data as shown in demo_dta.txt and set Static Point in data which is the First Point from Orientation line in data (last line) and its value (X, y, H), also it is possible to tweek Sigma errors in code like Sigma of Distances and Gons, it should be corrected to your data in lines 884 and 885 from your Total Station

---

# Input Data
Input data consists of, name of gon like 'T1-T2-T3' and value in grads, after all gons are writen then distances like 'T1-T2' and value in meters and finally the orientation of the network like 'T6-T5-T7-T8' and the value of the static point and its height '480446.037 4203353.345 339.5605', the input data should be as shown in demo_data.txt or like this

T7-T5-T6 84.4524 <br/>
T5-T6-T8 131.0599 <br/>
T6-T8-T7 75.6189 <br/>
T8-T7-T5 108.8644 <br/>
T5-T6 77.315 <br/>
T6-T8 211.788 <br/>
T8-T7 127.366 <br/>
T7-T5 206.550 <br/>
<br/>
T6-T5-T7-T8 <br/>
480446.037 4203353.345 339.5605 <br/>

Static Point is T6 in this example <br/>
Line 884 and 885 tweek Sigma erros

---

![alt text](https://github.com/nikos230/Horizonal-Network-Geodesy/blob/main/sxedio.jpg)
![alt text](https://github.com/nikos230/Horizonal-Network-Geodesy/blob/main/hor_net_1.jpg)
![alt text](https://github.com/nikos230/Horizonal-Network-Geodesy/blob/main/hor_net_2.jpg)

---

# Improvments, bugs and suggestions
If you like to suggest anything on this scirpt please contact me in nikolas619065@gmail.com
