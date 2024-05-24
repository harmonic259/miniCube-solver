# miniCube-solver
In this project $2\times2\times 2$  rubik (mini cube) solver was implemented using IDS-DFS, A*, BiBFS algorithms<br /> 
## Testing
7 testcases were considered (1.txt, 2.txt, ..., 7.txt in order of complexity) and you can test each algorithm (method) with each testcase using following command:

```
python main.py --testcase testcases/[Testcase] --method [Method]
```

Ther results show that BiBFS performs significantly better than two others (solves 7.txt in 175s while others solve 4.txt in more than 200s)

<details>
<summary>Results</summary>
  
![image](https://github.com/harmonic259/miniCube-solver/assets/88043179/f2a8e700-0057-4be7-af55-e1cf7fd0d7a6)
![image](https://github.com/harmonic259/miniCube-solver/assets/88043179/59c3a0e6-e11a-4f8d-ab50-202df34e34ad)
![image](https://github.com/harmonic259/miniCube-solver/assets/88043179/42d21f6a-a973-4947-b112-34cb3cec93b2)
![image](https://github.com/harmonic259/miniCube-solver/assets/88043179/9d6e6f6d-eff6-4d3c-813e-e4962adce825)
![image](https://github.com/harmonic259/miniCube-solver/assets/88043179/95581e6b-3b33-4293-a6cf-c8473500cac4)
![image](https://github.com/harmonic259/miniCube-solver/assets/88043179/2b2c6db0-381d-4dde-b9a3-9fabe470f174)

</details>
