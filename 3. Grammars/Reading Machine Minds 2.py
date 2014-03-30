# Reading Machine Minds 2
#
# We say that a finite state machine is "empty" if it accepts no strings.
# Similarly, we say that a context-free grammar is "empty" if it accepts no
# strings. In this problem, you will write a Python procedure to determine
# if a context-free grammar is empty.
#
# A context-free grammar is "empty" starting from a non-terminal symbol S 
# if there is no _finite_ sequence of rewrites starting from S that
# yield a sequence of terminals. 
#
# For example, the following grammar is empty:
#
# grammar1 = [ 
#       ("S", [ "P", "a" ] ),           # S -> P a
#       ("P", [ "S" ]) ,                # P -> S
#       ] 
#       
# Because although you can write S -> P a -> S a -> P a a -> ... that
# process never stops: there are no finite strings in the language of that
# grammar. 
#
# By contrast, this grammar is not empty: 
#
# grammar2 = [
#       ("S", ["P", "a" ]),             # S -> P a
#       ("S", ["Q", "b" ]),             # S -> Q b
#       ("P", ["P"]),                   # P -> P
#       ("Q", ["c", "d"]),              # Q -> c d 
#
# And ["c","d","b"] is a witness that demonstrates that it accepts a
# string.
#
# Write a procedure cfgempty(grammar,symbol,visited) that takes as input a
# grammar (encoded in Python) and a start symbol (a string). If the grammar
# is empty, it must return None (not the string "None", the value None). If
# the grammar is not empty, it must return a list of terminals
# corresponding to a string in the language of the grammar. (There may be
# many such strings: you can return any one you like.) 
#
# To avoid infinite loops, you should use the argument 'visited' (a list)
# to keep track of non-terminals you have already explored. 
#
# Hint 1: Conceptually, in grammar2 above, starting at S is not-empty with
# witness [X,"a"] if P is non-empty with witness X and is non-empty with
# witness [Y,"b"] if Q is non-empty with witness Y. 
#
# Hint 2: Recursion! A reasonable base case is that if your current
# symbol is a terminal (i.e., has no rewrite rules in the grammar), then
# it is non-empty with itself as a witness. 
#
# Hint 3: all([True,False,True]) = False
#         any([True,True,False]) = True

# symbol = start symbol
def cfgempty(grammar,symbol,visited):
  if symbol in visited:
    return None

  # check if symbol has any rules in grammar. If not, 'symbol' is terminal
  elif not any([rule[0] == symbol for rule in grammar]):
    return [symbol]

  else:
    new_visited = visited + [symbol] # update visited

    # consider every rewrite rule: 'symbol' -> RHS
    valid_destination_rhs = [r[1] for r in grammar if r[0] == symbol]
    for rhs in valid_destination_rhs:
      # check if every part of RHS is non-empty
      if all([None != cfgempty(grammar, r, new_visited) for r in rhs]):
        # if valid, create an example
        result = []
        for r in rhs:
          result += cfgempty(grammar, r, new_visited)
        return result
  return None


  # # print symbol
  # # print grammar

  # grammar_symbols = [x[0] for x in grammar]
  # # print grammar_symbols

  # for i in range(len(grammar)):
  #   print 'i is happening!', i

  #   # match symbol with corresponding grammar
  #   if symbol == grammar[i][0]:
  #     visited.append(grammar[i])
  #     # print visited

  #     output = grammar[i][1]


  #     for n in range(len(output)):
  #       # first_indexes = [y[i] for y in grammar]

  #       # cannot have for-loop in lambda?

  #       # find possible destinations if not terminal character
  #       if output[n] in grammar_symbols:
  #         possible_destinations = filter(lambda (x): x[0]==output[n] and x not in visited, grammar)

  #         print 'output is', output
  #         print 'output[n] is', output[n]
  #         print 'possible_destinations are', possible_destinations

  #         if possible_destinations == []:
  #           return None

  #         for dest in possible_destinations:
  #           if dest not in visited:
  #             symbol = dest[0]
  #             print 'output[n] is being evaluated', output[n]
  #             output[n] = cfgempty(grammar, symbol, visited)
  #             print 'output[n] evaluated to', output[n]
  #           # What is the case that it returns None? If any case leads to a dead end.
  #           # If anything in final output is "None", simply return None.
  #       # else if output[n] 

  #   return output[n]


  #       # print n in grammar_symbols
  #       # print destination not in visited
  #       # print ''
  #       # if (n in grammar_symbols and destination not in visited):
  #       #   print n, grammar[i]
  #         # return cfgempty(grammar, n, visited)
  #       # print """
  #       #   """
  #         # print 'output is', output
  #         # return output

  #   # stop iterating once you find a match -- this might not work
  #   # if only another grammar pattern other than the first valid one works...
    

# We have provided a few test cases for you. You will likely want to add
# more of your own. 

grammar1 = [ 
      ("S", [ "P", "a" ] ),           
      ("P", [ "S" ]) ,               
      ] 
                        
print cfgempty(grammar1,"S",[]) == None 

grammar2 = [
      ("S", ["P", "a" ]),             
      ("S", ["Q", "b" ]),             
      ("P", ["P"]), 
      ("Q", ["c", "d"]),              
      ] 

print cfgempty(grammar2,"S",[]) == ['c', 'd', 'b']


grammar3 = [  # some Spanish provinces
        ("S", [ "Barcelona", "P", "Huelva"]),
        ("S", [ "Q" ]),
        ("Q", [ "S" ]),
        ("P", [ "Las Palmas", "R", "Madrid"]),
        ("P", [ "T" ]),
        ("T", [ "T", "Toledo" ]),
        ("R", [ ]) ,
        ("R", [ "R"]), 
        ]

print cfgempty(grammar3,"S",[]) == ['Barcelona', 'Las Palmas', 'Madrid', 'Huelva']
