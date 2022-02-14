#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 13 18:00:21 2022

@author: applehome
"""

def num_prime():
    
    n=int(input ('Add n :'))
    track_input = []
    
    count = 0
   
    
    for i in range(2,n+1):
        #print ('******** Value of i = ', i ,'********')
        l=0
        for k in range(2,i-1):
            
            if i%k ==0:
                #print ('value of i == ',i, 'value of k ==',k)
                l=1
                break
            
            
            else:
            
                pass
            
        if l==0:
            track_input.append(i)
            
            
            count+=1
            #print('value of count :', count)
    
    #count=count -1  # If range of i is set from (1,n)
    #count= count -2, if therange of i is set from (0,n)
    
    print (track_input)
    print('Total number of prime numbers are' ,  count)


num_prime()