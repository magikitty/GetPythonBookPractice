"""
This is Lesson 22: Advanced operations with functions
Get Programming: Learn to Code With Python

The following is practice for returning a function object from another function
Based on Listing 22.9
"""

# Practice 1
def grumpy_cat():
    print("I'm a grumpy cat!")
    def no_n_times(n):
        print("No having fun. No", n, "times...")
        def no_m_times(m):
            print("...and no", m, "more times.")
            for _ in range(n+m):
                print("No!")
        return no_m_times
    return no_n_times

grumpy_cat()(5)(3)

# Practice 2
def fluffy_bunny():
    print("I'm a fluffy little bunny!")
    def do(verb):
        print("I like to " + verb + " all day long!")
        def num_times(num):
            print("I " + verb, num, "times every day!")
        return num_times
    return do

fluffy_bunny()("hippety hoppety bopetty")(10)