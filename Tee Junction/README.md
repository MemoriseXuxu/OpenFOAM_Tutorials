ANSYS版本是2022R1，OpenFOAM是com的v2106  
进口流速是10m/s，湍动能k为0.375.Omege为2567.201，采用KOmegaSST模型，瞬态计算，网格采用ANSYS Mesher生成  
算例主要为了比较Fluent和OpenFOAM的设置，本人之前多采用Fluent计算，OpenFOAM为新使用计算软件，通过Fluent软件验证OpenFOAM平台设置及计算的准确性。
Fluent中设置均为默认设置，对Wall处Roughness均设置为0，速度进口10m/s，两个压力出口。


![Velocity](https://github.com/MemoriseXuxu/OpenFOAM_Tutorials/blob/master/Tee%20Junction/Contour_U.jpeg)
![VelocityCompareAtX](https://github.com/MemoriseXuxu/OpenFOAM_Tutorials/blob/master/Tee%20Junction/Compare_UatX.jpeg)  


[U_Animation](https://user-images.githubusercontent.com/48404183/157583052-d07031c6-4ca6-428c-94db-678e6c5b19a3.mp4)  

[Pressure_Animation](https://github.com/MemoriseXuxu/OpenFOAM_Tutorials/blob/master/Tee%20Junction/Pressure_Video.mp4?raw=true)

