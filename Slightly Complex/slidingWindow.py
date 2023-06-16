def window(s, chars):

	hash = {}
	for c in chars:
		hash[c] = 1

	#this hash will keep account of how many characters we have knocked off. Each key will represent a character in chars
	# each one is represented as 1, and will lower it to 0 when fulfilled

	#the counter is made to measure the string length against
	counter = len(chars)
	start = 0
	end = 0
	sub_size = len(s) + 1
	head = 0

	while end < len(s):

		#this is the "continue" section. Keep this running where there are more elements in s to process
		if s[end] in hash:				#we have found a letter
			if hash[s[end]] > 0:
				counter -= 1			#modify the length counter. We can use this as part of the substring
			hash[s[end]] -= 1			#amend the hash to say that we've gotten this character

		#what do we do if we have what we need
		while counter == 0:

      #calculate the current substring size once we want the minimum
			if end - start + 1 < sub_size:
				sub_size = end - start + 1
				head = start

    #keep shrinking to get the minimum size

			if s[start] in hash:
				hash[s[start]] +=1			#This is a character we need

				if hash[s[start]] > 0:      # Make this invalid. This is clearly not a character we want
					counter += 1
			start += 1
	# keep expanding and shortening here
		end +=1

	return "" if sub_size == len(s) + 1 else s[head : head + sub_size]

print("\n")
print(window("lieurhgaieug", "hg"))
print("\n")
