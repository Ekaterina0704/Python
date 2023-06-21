
def find_fathest_orbit(orbits):
    list_of_elip_orbit=[i for i in orbits if i[0]!=i[1]]
    list_of_arias=[i[0]*i[1] for i in list_of_elip_orbit]
    max_area_index=list_of_arias.index(max(list_of_arias))
    return list_of_elip_orbit[max_area_index]
                
list_of_orbits=[(1,3),(2.5,10), (7,2), (6,6), (4,3)]
print(find_fathest_orbit(list_of_orbits))


# def find_fathest_orbit(orbits):
# return max(orbits,key=lambda x: x[0]*x[1] if x[0]!=x[1] else -1)