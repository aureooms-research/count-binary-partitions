# import functools

# @functools.lru_cache(maxsize=None)
# def P ( N , k ) :
	# if N == 0 :
		# return 1
	# elif k == 0 :
		# return 0
	# elif N % 2 :
		# return P ( N - 1 , k )
	# else :
		# return P ( N - 1 , k ) + P ( N // 2 , k - 1 )

# def b ( n ) :
	# return P ( 2**n , n + 1 )

import sys

n = int(sys.argv[1])

Q = [ [ 0 ] ] + [ [ 0 ] * (2**(k-1)+1) for k in range( 1 , n + 2 ) ]

# could use only the last two rows instead of n+2
# that would be faster
for k in range( n + 2 ) :
	Q[k][0] = 1

for k in range ( 1 , n + 2 ) :

	for i in range( 1 , 2**(k-1) + 1 ) :

		if i % 2 :
			Q[k][i] = Q[k][i-1]
		else :
			Q[k][i] = Q[k][i-1] + Q[k-1][i//2]

print( Q[n+1][2**n] )
