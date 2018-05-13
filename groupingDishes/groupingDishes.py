def groupingDishes(dishes):
	
    ingredients = []
    for d in dishes:
        for f in [f for f in d[1:]]:
            if f not in ingredients:
                ingredients.append(f)
                
    
    ingredients = sorted(list(set(ingredients)))
    d = {}
    
    for i in ingredients:
        d[i] = []
        
    for dis in dishes:
        for i in dis[1:]:
            d[i].append(dis[0])
            
    
    for key in d:
    	d[key] = sorted(d[key])
    
    for k in ingredients:
        print(k)
        if len(d[k]) == 1:
            d.pop(k, None)
            
            
    output = []
    for i in ingredients:
        if i in d:
            tmp = []
            tmp.append(i)
            for dis in d[i]:
                tmp.append(dis)
            output.append(tmp)
        
        
    return output
        
