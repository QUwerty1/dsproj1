class Logger:
    def log(self, message):
        with open('logs/' + message.channel.name + '.txt', mode='a') as f:
            f.write(f'{message.author.name}: {message.content} || {message.created_at} \n')
