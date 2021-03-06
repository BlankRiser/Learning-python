# Learning Python

This repository will contain all the source code of python projects that I work on. 

# Resources

[Google Collab](https://colab.research.google.com/)

[Setting up Sublime Text 3](https://realpython.com/setting-up-sublime-text-3-for-full-stack-python-development/#themes)

# Basics of Python
- Python was developed by Guido Van Rossum and named it after the “Monty Python”, a British surreal comedy group.
- Officially launched in 1991 in Netherlands
- It is derived from CPP, Perl, Modulo 3, and successor of ABC Language.
- It's case sensitive.
- It's dynamically typed language.
- Features of python
    1. Simple and easy to learn
    2. Freeware and open source
    3. High level programming language
    4. platform independent
    5. Dynamically typed
    6. Portability
    7. Supports extensive libraries
    8. Flavors of python : Cython, IronPython, Jython.

## Code


1. To know the amount of keywords in python
```python
    import keyword
    keyword.kwlist
    # Total of 33
```
- **Datatypes**: 14 types, 5 are fundamental : Int, Float, String, Boolean, Complex. The others are: List, Tuple, Dictionary, Set, Frozen Set, Bytes, Byte Array, Range, None.

```python
    a=10
    print(type(a))
    #type lets you know the type of datatype a variable is associated with
    
    id(a)
    #id lets you know the memory location of 10(not a).

    int
    a = 10
    hex(a) # 0xa -> begins with 0x
    bin(a) # 0b1010 -> begins with 0b
    oct(a) # 0o12 -> beginswith 0o
    # all belong to <class 'str'> after conversion
    
    float
    a = 10.5
    #can't covert to oct,dec, hex
    
    str
    a="Ram bro"
    len(a) => 7
    a.split(" ") => ['Ram', 'bro']
    # Splicing of string
    a[:] #=> ['Ram', 'bro']
    a[1:3] #=> 'am'
    a[::-1] #=> 'orb maR' str reversal
    a[-5:-1] #=> 'm br' reverse string index
    a[1:6:3]#=> 'ab' it takes each value after 3 steps
    
    bool
    print(True+True) # 2
    print(True+False) # 1
    print(False + False) # 0  
    print(True) # 1
    print(False) # 0
    
    complex (a+bj)
    a=10 + 20j
    
    list [a,b,c]  #Mutable
    a= [10,20,30]
    a.append(40) # appends 40 to a
    
    
    tuple (a,b,c) #Immutable
    
    set {a,b,c} # doesn't preserve order in the session
    a={10,20,30}
    a.add(40) # adds element
    
    dict {key:value} # key must be unique
    a={'a':1,'b':2.5,'c':'char'}
    a.keys() #=> dict_keys(['a', 'b'])
    a.values() #=> dict_values([1, 2])
    
    frozenset #immutable version of a set
    vowels = {'a', 'e', 'i', 'o', 'u'}
    fSet = frozenset(vowels)
    fSet #=> frozenset({'a', 'e', 'i', 'o', 'u'})
    
    range # (start, stop[, step])
    a= range(10) # 0,1,2,3,4,5,6,7,8,9
    type(a) # range(0,9)
```    
    

- **Input**
```python
    a = input("Give input: ")
    # a gets the input as str
    
    a = eval(input("give int: "))
    # eval() evaluates the input to their correct types
    # i/p: 23 type(a): int
    b = eval(input("give float: "))
    # i/p: 3.57 type(b): float
    c = eval(input("give str:: "))
    # i/p: "hello" type(c): str
    d = eval(input("give tuple "))
    # i/p: 1,2 or (1,2) type(d): tuple
    e = eval(input("give list "))
    # i/p: [1,2] type(e): list
```
- **Operations and Operators**
```python
    '''
    Arithmetic Operators
    Relational/Comparison Operators
    Logical Operators
    Bitwise operators
    Assignment Operators
    Special Operators
    '''
    
    a=2
    b=5
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)
    print(a**b) # power
    
    a="hello"
    b=5
    a*b # 'hellohellohellohellohello'
    
    # Relational
    a=2
    b=5
    a > b # False
    a < b # True
    a == b # False
    a != b # True
    a <= b # True
    a >= b # False
    
    a="rat"
    b="rama"
    a > b # True, coz t > m, it compares char from L to R
    a < b # False, same for others
```    

- ***Control Flow Statement:***
    1. Conditional: If, Else, Elif
    2. Iterative: While, For
    3. Transfer: Break, Continue, Pass

- **OOPs**
```python
    class Person:
      def __init__(self, name, age):
        self.name = name
        self.age = age
    
      def myfunc(self):
        print("Hello my name is " + self.name)
    
    p1 = Person("John", 36)
    p1.myfunc()
    
    '''
    The self parameter is a reference to the current instance of the class, 
    and is used to access variables that belongs to the class.
    It does not have to be named self , you can call it whatever you like, 
    but it has to be the first parameter of any function in the class:
    
    __init__ is like a constructor:
    '''
    
    class Person:
      def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age
    
      def myfunc(abc):
        print("Hello my name is " + abc.name)
    
    p1 = Person("John", 36)
    p1.myfunc()
```
 

**Encapsulation: Public, Protected, Private**

variable without underscore is Public : self.variable

variable with underscore is Protected : self._variable

variable with 2 underscore is Private : self.__variable
```python
    class Robot(object):
       def __init__(self):
          self.a = 123 # Public
          self._b = 123 # Protected
          self.__c = 123 # Private
    
    obj = Robot()
    print(obj.a)
    print(obj._b)
    print(obj.__c) # error occurs as it's private
```

To install packages directly from jupyter notebook, use !
`!pip install <package_name>`

**Warning**

To ignore warnings
```python
    import warnings
    warnings.filterwarnings("ignore")
```
# Pandas

```python

    import pandas as pd
    
    file = pd.read_csv("file.csv")
    file.head(10) # shows first n rows
    
    file.shape # no. of rows and columns of the file
    file.describe() # does all statistics operations on the file
    file.isnull() # detects missing values in the file
    file.isnull().sum() # summarizes all the missing data
    file.dtypes # returns all the datatypes in the file 
    file.<column name> # shows the column mentioned
    
    #Opening excel file
    data = pd.read_excel('Dataset.xlsx',Sheet_name = "sheet1")
    
    #Check the total number of rows with incomplete data
    file.isnull().sum()
    
    #Remove row with incomplete data
    file.dropna(inplace=True) # inplace makes the operaion permanent on file
    
    # Remove column
    file.drop(columns="[<Column_Name1>,<cn2>,<cn3>]", inplace = True, axis =1)
    
    # Filling missing data using mean and mode
    file['<column1>'].fillna(file['<column1>'].mode(),inplace=True)
    file['<column2>'].fillna(file['<column2>'].mode(),inplace=True) # both mean and mode is done for float columns
    file['<column2>'].fillna(file['<column2>'].mean(),inplace=True) # both mean and mode is done for float columns
    file.isnull().sum() # will show all columns are filled and 0 null columns
    
    # plotting a graph
    #bar graph
    graph = file['<column name>'].value_counts().plot(kind = 'bar',figsize = (14,8), title = "title of graph")
    graph.set_xlabel("X Label")
    graph.set_ylabel("Y Label")
    
    # Other method to plot graph
    spenders.groupby('Level')['Level'].agg('count').plot.bar()
```    

# Numpy

- stands for numerical python.
- provides powerful n-dimensional array object.
- We use numpy array because they consume less memory, are fast and convenient.

```python
    np.ones()
    np.zeros(10) #>array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])
    # creaes null vector of size 10
    
    np.ones(10) #array([1., 1., 1., 1., 1., 1., 1., 1., 1., 1.])
    # creaes vector with 1's of size 10
    
    np.arange(5,20) #>array([ 5,  6,  7,  8,  9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19])
    #creagtes a vector from 5 to 19
    
    np.arange(9).reshape(3,3) # reshapes into 3X3 matrix
    '''
    array([[0, 1, 2],
           [3, 4, 5],
           [6, 7, 8]])
    '''
    np.nonzero([0,1,0,0,5,7,4,0,0]) #>(array([1, 4, 5, 6], dtype=int64),)
    # gives indices of non-zero values in array
    
    np.eye(n) # creates n X n identity matrix 
    np.eye(3) # array([[1., 0., 0.], [0., 1., 0.],[0., 0., 1.]])
    
    np.random.random((3,3))
    
    a = np.random.random((10,10))
    amin,amax = a.min(),a.max() # gives the max and min of a
    amean = a.mean() # mean
    
    #Create a 2D matrix with only 1 as borders
    a = np.ones((10,10))
    a[1:-1,1:-1]=0
    '''
    array([[1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
           [1., 0., 0., 0., 0., 0., 0., 0., 0., 1.],
           [1., 0., 0., 0., 0., 0., 0., 0., 0., 1.],
           [1., 0., 0., 0., 0., 0., 0., 0., 0., 1.],
           [1., 0., 0., 0., 0., 0., 0., 0., 0., 1.],
           [1., 0., 0., 0., 0., 0., 0., 0., 0., 1.],
           [1., 0., 0., 0., 0., 0., 0., 0., 0., 1.],
           [1., 0., 0., 0., 0., 0., 0., 0., 0., 1.],
           [1., 0., 0., 0., 0., 0., 0., 0., 0., 1.],
           [1., 1., 1., 1., 1., 1., 1., 1., 1., 1.]])
    '''
    
    #Undestanding NaN
    print(0*np.nan) # nan
    print(np.nan == np.nan) # False
    print(np.inf > np.nan) # False
    print(np.nan - np.nan) # nan
    print(0.3 == 3*0.1) # False
    
    #Diagonal elements
    a=np.deiag(np.arang(4))
    a = np.diag(1+np.arange(4),k=0) 
    # k decides from which column the first diagonal is taken
    
    # create a 8*8 matrix, implement a chess-board pattern
    c = np.zeros((8,8),dtype=int)
    c[1:2,::2] = 1
    c[::2,1::2] = 1
    
    #Making an array immutable
    a = np.zeros(10)
    a.flags.writeable =False # makes a immutable

```

# Data Visualization: Matplotlib and Seaborn


[Data Visualization using Matplotlib](https://towardsdatascience.com/data-visualization-using-matplotlib-16f1aae5ce70)

[Data Visualization using Seaborn](https://towardsdatascience.com/data-visualization-using-seaborn-fc24db95a850)

```python

    import matplotlib.pyplot as plt
    
    x = np.arange(0,4*np.pi,0.1) # 0.1 is the step
    y = np.tan(x)
    plt.plot(x,y)
    plt.show()
    
    # Scatter data
    plt.scatter(dataX,dataY)
    
    # To set title and labels
    plt.title(' Title Name ')
    plt.xlabel('X Axis Label')
    plt.ylabel('Y Axis Label')
    plt.legend('<char>') # character that tell you what the point is
    
    #using pandas to plot
    file.plot(kind = 'scatter', x='<column1>', y= '<column2>')
    plt.show()
    
    # visualizing using Seaborn
    import seaborn as sns
    sns.FacetGrid(data=file, hue ='<columnName>',height = 5).map(plt.scatter, '<column1>','<column2>').add_legend()
    plt.show()
    
    #boxplot
    sns.boxplot(x='<column1>', y ='<column2>', data = file)
    plt.show() # the points not in the box region are outliers
    
    #violin plot : denser regions are fatter & sparser regions are thinner
    sns.violinplot(x='<column1>', y='<column2>', data = file)
    plt.show() # this plot indicates the median value( the white middle dot )
    
    #kernel density plot : utlizes and creates an estimate of kernel density of the underlying features.
    sns.FacetGrid(data = file, hue = 'Species', height = 5).map(sns.kdeplot,'PetalLengthCm').add_legend()
    plt.show()
    
    #pair plot : bivariate relation between each pair of features
    sns.pairplot(file.drop("<column1>",axis =1),hue='<column2>',height=3)
    plt.show()
```
