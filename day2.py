# shape point is index+1 actually
# rps is modular S->P->R->S
# loops in mod 3
def solve(f):
   sum=0
   for line in f:
      player1,player2 = line.split()
      player1 = "ABC".index(player1)
      player2 = "XYZ".index(player2)
      sum += player2+1 
      match (player2-player1) % 3:
         case 1:
            sum += 6
         case 0:
            sum += 3
   return sum
      
def solve2(f):
   sum=0
   for line in f:
      player1,result = line.split()
      player1 = "ABC".index(player1)
      match (result):
         case 'X': #lose
            sum += ((player1-1)%3)+1
         case 'Y': #draw
            sum += (player1+4)
         case 'Z': #win
            sum += ((player1+1)%3)+7
   return sum

filename = 'day2.input'
mode = 'r'
f = open(filename, mode)
print(solve(f))
f.seek(0, 0)
print(solve2(f))