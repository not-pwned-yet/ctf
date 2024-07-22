# README

## Starship

We've gotten console access to the rogue ship, but there isn't much time left. Hopefully you can figure out how to destroy it... before it's too late.

### Solving

It's kinda weird to get the flag that based on luckiness. Anyway, the solving steps are:

1. Run the netcat
2. Input 1 to show the dataset
3. Input 4 to show the prediction, it always shows enemy but we have to make it as friendly so..
4. Input 42 as the hidden menu. Then, input the last output from the 3rd step and make it friendly by adding the x,y,yada yada and add friendly
5. Train the model by inserting 2 as the input
6. Insert 4, if we lucky enough, the both output are showing friendly and we get the flag

```bash
$ nc starship.chal.imaginaryctf.org 1337
== proof-of-work: disabled ==
1<[ missle defense system control panel ]>
1. show dataset
2. train model
3. predict state
4. check incoming objects
initializing...
>
--- BEGIN DATASET ---
x,y,velocity,rotation,price,rizz,anger,patience,aura,classification
80,12,68,77,75,29,74,30,70,enemy
47,8,20,115,33,27,30,49,35,friendly
45,-2,48,91,-2,7,39,42,19,friendly
17,-20,-7,98,0,36,53,40,64,friendly
20,34,42,98,4,42,-1,68,51,friendly
60,10,44,117,68,72,115,46,108,enemy
53,-27,69,69,32,80,61,28,57,enemy
64,-16,67,80,6,69,73,92,95,enemy
64,26,40,98,40,64,95,36,108,enemy
103,-6,70,67,8,42,92,83,118,enemy
72,5,92,84,29,82,110,62,109,enemy
39,-32,37,90,35,21,26,90,23,friendly
59,17,37,79,13,47,65,96,91,enemy
116,-16,30,96,35,91,99,44,88,enemy
56,27,39,79,7,97,89,44,111,enemy
77,-29,47,109,38,7,36,49,76,friendly
73,1,15,95,-10,15,-6,101,50,friendly
67,14,87,102,66,83,54,46,81,enemy
56,-18,47,85,12,40,43,81,79,friendly
59,8,71,91,53,83,103,95,72,enemy
56,13,45,127,-13,2,33,80,69,friendly
107,-22,53,117,22,89,102,57,56,enemy
70,18,0,117,-3,24,0,46,47,friendly
63,27,-11,126,17,2,15,66,62,friendly
35,10,48,115,-28,-10,52,51,19,friendly
80,-28,32,74,53,61,115,53,88,enemy
17,-32,24,106,10,26,-15,91,53,friendly
78,16,-3,134,-8,38,36,99,53,friendly
58,21,36,86,-18,34,20,51,79,friendly
88,-30,42,85,55,58,95,38,121,enemy
66,-28,83,62,64,94,116,51,68,enemy
27,-20,24,98,37,25,39,46,58,friendly
22,13,40,85,17,49,17,100,54,friendly
60,-28,48,79,12,10,25,56,41,friendly
83,-18,31,103,-31,-5,51,69,53,friendly
107,-7,40,48,71,87,54,91,99,enemy
70,3,8,83,-12,-1,7,88,47,friendly
77,4,69,68,24,39,68,90,76,enemy
21,-32,-1,88,-22,26,17,49,41,friendly
42,-14,40,74,36,-16,49,84,15,friendly
21,-15,10,98,-5,2,-7,55,37,friendly
58,-1,31,79,70,53,81,60,61,enemy
75,5,29,84,24,68,115,35,98,enemy
36,14,7,126,-7,48,48,49,67,friendly
104,-31,61,76,49,29,69,55,85,enemy
63,-15,30,115,10,92,114,79,97,enemy
79,-7,39,116,21,48,85,35,65,enemy
76,16,44,85,63,69,91,95,124,enemy
26,5,32,107,-27,51,44,40,36,friendly
118,38,75,72,18,70,103,70,117,enemy
88,31,75,104,61,75,54,62,78,enemy
72,-35,21,95,-11,28,26,89,62,friendly
88,22,58,82,48,62,108,43,82,enemy
78,10,1,75,9,45,-2,39,52,friendly
71,-27,55,73,45,60,70,29,64,enemy
76,5,9,116,37,25,14,33,32,friendly
76,18,17,103,19,52,53,92,27,friendly
110,-3,74,62,50,28,82,78,124,enemy
43,30,30,93,-19,39,15,68,37,friendly
99,28,28,88,46,79,82,95,54,enemy
--- END DATASET ---
> 4
target 1: 57,34,12,74,87,100,6,11,66 | result: enemy
target 2: 84,12,15,57,40,65,41,17,80 | result: enemy
> 42
enter data: 57,34,12,74,87,100,6,11,66,friendly
> 2
model trained!
> 4
target 1: 57,34,12,74,87,100,6,11,66 | result: friendly
target 2: 84,12,15,57,40,65,41,17,80 | result: friendly
flag: ictf{m1ssion_succ3ss_8fac91385b77b026}
>
```

**Flag:** `ictf{m1ssion_succ3ss_8fac91385b77b026}`
