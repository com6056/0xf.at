import telnetlib

HOST = '212.17.118.125'
PORT = '2727'

tn = telnetlib.Telnet(HOST, PORT)

tn.read_until(b'To start the game send me: GO')
tn.write(b'GO')
problem = tn.read_until(b'=?')
problem = str(problem)
problem = problem[4:len(problem) - 3]
answer = str(eval(problem))
tn.write(answer.encode('ascii'))
tn.read_until(b'Correct!')
problem = tn.read_until(b'=?')
problem = str(problem)
problem = problem[4:len(problem) - 3]
answer = str(eval(problem))
tn.write(answer.encode('ascii'))
tn.read_until(b'Correct!')
problem = tn.read_until(b'=?')
problem = str(problem)
problem = problem[4:len(problem) - 3]
answer = str(eval(problem))
tn.write(answer.encode('ascii'))
tn.read_until(b'Correct!')
problem = tn.read_until(b'=?')
problem = str(problem)
problem = problem[4:len(problem) - 3]
answer = str(eval(problem))
tn.write(answer.encode('ascii'))
tn.read_until(b'Correct!')
problem = tn.read_until(b'=?')
problem = str(problem)
problem = problem[4:len(problem) - 3]
answer = str(eval(problem))
tn.write(answer.encode('ascii'))
tn.read_until(b'Correct!')
problem = tn.read_until(b'=?')
problem = str(problem)
problem = problem[4:len(problem) - 3]
answer = str(eval(problem))
tn.write(answer.encode('ascii'))
tn.read_until(b'Correct!')
problem = tn.read_until(b'=?')
problem = str(problem)
problem = problem[4:len(problem) - 3]
answer = str(eval(problem))
tn.write(answer.encode('ascii'))
tn.interact()
