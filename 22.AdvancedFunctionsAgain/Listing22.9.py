"""
This is Lesson 22: Advanced operations with functions
Get Programming: Learn to Code With Python

The following is practice for returning a function object from another function
Based on Listing 22.9
"""

# Practice 1
def grumpy():
    print("I am a grumpy cat!")
    def no_n_times(n):
        print("No having fun. No", n, "times...")
        def no_m_times(m):
            print("...and no", m, "more times.")
            for i in range(n+m):
                print("No!")
        return no_m_times
    return no_n_times

grumpy()(5)(3)