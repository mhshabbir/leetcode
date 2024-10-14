class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        """
        [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
        {"London": "New York",
          "New York":"Lima",
          "Lima","Sao Paulo"}
        


        """
        destination = ""
        pathMap = {}
        for path in paths:
            cityA, cityD = path
            pathMap[cityA] = cityD
        # print(pathMap)
    
        city = paths[0][0]
        while city in pathMap:
            city = pathMap[city]
        
        destination = city
        return destination