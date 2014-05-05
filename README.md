local-sensitivity-analysis
==========================

A small and quick command line tool for doing quick sensitivity calculations in agent-based models (ABMs). Mostly just (1) labor-saving device for me (2) experiment with argparse module and (3) a potential piece of a larger ABM sensitivity analysis program that I may make when I have more time.

In Steven F. Railsback and Volker Grimm's book *Agent-Based and Individual-Based Modeling: A Practical Introduction*, they advocate paying attention to model "currencies" that denote some observational values of interest produced by the model. For both model analysis and calibration of model procedures the modeler performs local sensitivty analysis to figure out how sensitive particular parameter values are to small changes. On page 293, they introduce a basic form of sensitivity analysis that can be used to find sensitivity above and below the reference value for a parameter. Usually, + or - 5% (*dP*) produces the value to vary the parameter of interest (*P*) by. For example, 5% of 80 is 4. Hence, if the modeler has a parameter set at the reference value of 80, they would vary it by 4 (76, 84). They would run it at the parameter value of 80 to get *C*, the currency value with the default parameter setting. By running it at 76 and 84, they would derive *Cminus* and *Cminus*, the currency values for lower and upper ranges of the amount they varied the model. 

To get the upper and lower sensitivity ranges for the parameter, the equations below are used:

*Splus* = (*Cplus* - *C*)/(*dP*/*P*)
 
*Sminus* = (*C* - *Cminus*/(*dp*/*P*)
 
This is obviously quite tedious to do by hand, particularly when one is doing very basic local sensitivity analysis sequentially on each parameter. Hence I wrote a tiny command line program for doing both equations at once. 

The user provides the following arguments as command line option-value pairs: 
  
