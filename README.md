local-sensitivity-analysis
==========================

A small and quick command line tool for doing quick sensitivity calculations in agent-based models (ABMs). Mostly just (1) labor-saving device for me (2) experiment with argparse module and (3) a potential piece of a larger ABM sensitivity analysis program that I may make when I have more time. It's quick and dirty and will be iteratively upgraded as time permits.

In Steven F. Railsback and Volker Grimm's book *Agent-Based and Individual-Based Modeling: A Practical Introduction*, they advocate paying attention to model "currencies" that denote some observational values of interest produced by the model. For both model analysis and calibration of model procedures the modeler performs local sensitivty analysis to figure out how sensitive particular parameter values are to small changes. On page 293, they introduce a basic form of sensitivity analysis that can be used to find sensitivity above and below the reference value for a parameter. Usually, + or - 5% (*dP*) produces the range to vary the parameter of interest (*P*) by. 

For example, 5% of 80 is 4. Hence, if the modeler has a parameter set at the reference value of 80, they would vary it by 4 (76, 84). They would run it at the parameter value of 80 to get *C*, the currency value with the default parameter setting. By running it at 76 and 84, they would derive *Cminus* and *Cplus*, the currency values for default parameter value - *dP* and default parameter + *dP*.

Railsback and Grimm state that +- 5% is just a rule of thumb. Sometimes it can be better to use a more contextually appropriate range to vary *P* by . Besides, they also point out the basic local sensitivity analysis template they provide is also more intended for conceptual purposes and/or basic calculations. For anything more advanced, they suggest the analyst consult more sophisticated techniques in the ABM and simulation and modeling literatures. However, for doing some basic local sensitivity analysis to get a sense of what's going on with the model, their simplified local sensitivity analysis procedure can still be useful. 

To get the upper and lower sensitivity for the parameter, Railsback and Grimm provide these equations below:

*Splus* = (*Cplus* - *C*)/(*dP*/*P*)
 
*Sminus* = (*C* - *Cminus*/(*dP*/*P*)
 
This is obviously quite tedious to do by hand, particularly when one is doing very basic local sensitivity analysis sequentially on each parameter. Hence I wrote a tiny command line program for doing both equations at once. 

After downloading the script to a desired present working directory and cd'ing to that folder in their command line terminal, the user inputs the following:

python localSA.py --Pn *parameter name* --P *default parameter value* --Dp *range to vary* --Cr *currency reference value* --Cp *upper currency value* --Cm *lower currency value*

After the desired inputs are provided, the program outputs the parameter name, default parameter value, paramater variance range, and upper and lower sensitivity values to the command line. 

Assuming your parameter name is "BallerStatus," your default parameter value is 100, you chose to vary it by 5, the upper model currency computed when BallerStatus is 105 is 702.83, and the lower model currency you got when you ran BallerStatus at parameter value 95 is 695.54, you would use this program with the following inputs:

python localSA.py --Pn BallerStatus --P 100 --Dp 5 --Cr 700 --Cp 702.83 --Cm 695.54

Unless all desired inputs (name of your parameter, the default parameter value, the +- range you are varying your parameter by, model currency when the parameter is varied up, and model currency when the parameter is varied down) provided, the script will return errors. 
