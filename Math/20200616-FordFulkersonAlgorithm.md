# Ford-Fulkerson Algorithm（FFA）  

### FFA能做什么？  
对于给定的流网络图G，尽量利用网络的载流能力，找到最优的路径网络，能承载最大的流量。  

流图（Flow Network）：  
- 是一个有向图   
- 每条边都有非负的载流容量值，即允许的最大流量  
- 仅有一个源点（Source Point），不断产生流量  
- 仅有一个沉点（Sink Point），不断吸收流量  

对于一个找到的路径网络f，每条边都承载着一定的流量，将流量从源点传送到沉点，并且满足：  
- 每条边都承载着非负的流量f(e)，并且不超过该边最大容量Ce  
- 除了源点和沉点，对于其他点，进入的流量等于出去的流量  

在给定的路径网络f下，流图G有对应有一个余图Gf（Remaining Graph）：  
- Gf与G有相同的顶点集  
- 如果(u,v)是G中的边，且f(e)<Ce，则在Gf中，边(u,v)的载流为Ce-Gf，称为前向边（forward edge）  
- 找路径有时可能需要“回退”，因此也需要后向边（backward edge），即(v,u)，流量值为f(e)  


### FFA算法  
```python
initialize f(e)=0 for all edges e in G
while there is a source->sink path P in the remaining graph Gf
    let b be the maximum flow through P
    for each edge (u,v) on P:
        if (u,v) is a forward edge:
            increase f(e) in G by b
        else:
            reduce f(e) in G by b
    update f to f'
    update the remaining graph Gf to Gf'
return f
```


### FFA算法证明  
pass  
