#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 00:03:25 2020
@author: parkerwray


This code defines functions that load and manipulate material data.

"""

import pandas as pd
import scipy as sci
import tkinter as tk
from tkinter import filedialog



class material():
    def __init__(self):
        
        self.n = []
        self.k = []
        self.data = []

    def refinfo(self, filename = None, unit = 'nm'):
    
        """
        Read .csv files from refractive index info and save into Pandas data frame 
        with collumns [lda, n, k]
        
        Inputs:
            filename: location of .csv file. If blank a gui will be used to select 
            the data file
            
            unit: unit of the wavelength data
            
        Outputs:
            self.n = interpolation function that interpolates n data based on 
            wavelength given a wavelength argument. I.e., mat1.n(400) gives n 
            at 400 unit

            self.k = interpolation function that interpolates k data based on 
            wavelength given a wavelength argument. I.e., mat1.k(400) gives k
            at 400 unit
            
            self.data = panda DataFrame of the raw [lda, n, k] data extracted.
        """
        if filename == None:
            filename = grab_file()
        
        test = pd.read_csv(filename)
        mask = pd.to_numeric(test.iloc[:,1], errors='coerce').isnull().cumsum();
        #test2 = [g[1:].rename(columns={0:g.iloc[0].values[0]}) for i, g in test.groupby(mask)]
        test2 = [g[1:].rename(columns={0:g.iloc[0].values[0]}).reset_index(drop=True) for i, g in test.groupby(mask)]
        test2[0] = test2[0].rename(columns={'wl':'lda'})
        test2[1] = test2[1].rename(columns={"wl":"lda", "n":"k"})
        test3 = pd.merge(test2[0], test2[1], on = 'lda').astype('float')
        
        test3.lda = {
                'nm': lambda x:x*1E3,
                'um': lambda x:x,
                'mm': lambda x:x*1E-3}[unit](test3.lda)
           
        self.n = sci.interpolate.interp1d(test3.lda, test3.n)
        self.k = sci.interpolate.interp1d(test3.lda, test3.k)    
        self.data = test3


def grab_file():
    root = tk.Tk()
    root.withdraw()
    return filedialog.askopenfilename()









