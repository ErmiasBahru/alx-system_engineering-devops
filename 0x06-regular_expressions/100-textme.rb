#!/usr/bin/env ruby
print ARGV[0].scan(/\[from:(.*?)\]/).join
print (",")
print ARGV[0].scan(/\[to:(.*?)\]/).join
print (",")
print ARGV[0].scan(/\[flags:(.*?)\]/).join
print ("\n")