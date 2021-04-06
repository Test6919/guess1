## Welcome to GitHub Pages

You can use the [editor on GitHub](https://github.com/Test6919/testrepos.github.io/edit/gh-pages/index.md) to maintain and preview the content for your website in Markdown files.

Whenever you commit to this repository, GitHub Pages will run [Jekyll](https://jekyllrb.com/) to rebuild the pages in your site, from the content in your Markdown files.

### Markdown

Markdown is a lightweight and easy-to-use syntax for styling your writing. It includes conventions for

```markdown
Syntax highlighted code block

# Header 1
## Header 2
### Header 3

- Bulleted
- List

1. Numbered
2. List

**Bold** and _Italic_ and `Code` text

[Link](url) and ![Image](src)
```

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/Test6919/testrepos.github.io/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://support.github.com/contact) and we’ll help you sort it out.
import discord

import os

import typing

import asyncio

import random

from discord.ext import commands

class games(commands.Cog):

  

  

  def __init__(self, client):

    self.client=client

    

    

  @commands.command()

  async def guess(self, ctx):

    number = random.randint(1, 20)

    for i in range(0, 20):

        await ctx.send('Guess a number between 0 and 20')

        def check(m):

          return m.author == ctx.author

        response = await self.client.wait_for('message', check=check)

        guess = int(response.content)

        if guess > number:

            await ctx.send("Your guess was __Greater__ than the original number :pensive:\n*Hint :- The original number is __Smaller__ than your guess!*\n```Chances Remaining :- 2```")

            response = await self.client.wait_for('message', check=check)

            guess = int(response.content)

            if guess > number:

              await ctx.send("Your guess was __Greater__ than the original number :pensive:\n*Hint :- The original number is __Smaller__ than your guess!*\n```Chances Remaining :- 1```")

              response = await self.client.wait_for('message', check=check)

              guess = int(response.content)

              if guess > number:

                await ctx.send(f"Your guess was __Greater__ than the original number :pensive:\nThe Original number was {number}")

                return

              elif guess < number:

                await ctx.send(f"Your guess was __Smaller__ than the original number :pensive:\nThe Original number was {number}")

                return

              else:

                await ctx.send(f'Bingo! You guessed it!:tada:\nThe number was {number}')

                return

            elif guess < number:

              await ctx.send("Your guess was __Smaller__ than the original number :pensive:\n*Hint :- The original number is __Greater__ than your guess!*\n```Chances Remaining :- 1```")

              response = await self.client.wait_for('message', check=check)

              guess = int(response.content)

              if guess > number:

                await ctx.send(f"Your guess was __Greater__ than the original number :pensive:\nThe Original number was {number}")

                return

              elif guess < number:

                await ctx.send(f"Your guess was __Smaller__ than the original number :pensive:\nThe Original number was {number}")

                return

              else:

                await ctx.send(f'Bingo! You guessed it!:tada:\nThe number was {number}')

                return

            else:

              await ctx.send(f'Bingo! You guessed it!:tada:\nThe number was {number}')

              return    

        elif guess < number:

            await ctx.send("Your guess was __Smaller__ than the original number :pensive:\n*Hint :- The original number is __Greater__ than your guess!*\n```Chances Remaining :- 2```")

            response = await self.client.wait_for('message', check=check)

            guess = int(response.content)

            if guess > number:

              await ctx.send("Your guess was __Greater__ than the original number :pensive:\n*Hint :- The original number is __Smaller__ than your guess!*\n```Chances Remaining :- 1```")

              response = await self.client.wait_for('message', check=check)

              guess = int(response.content)

              if guess > number:

                await ctx.send(f"Your guess was __Greater__ than the original number :pensive:\nThe Original number was {number}")

                return

              elif guess < number:

                await ctx.send(f"Your guess was __Smaller__ than the original number :pensive:\nThe Original number was {number}")

                return

              else:

                await ctx.send(f'Bingo! You guessed it!:tada:\nThe number was {number}')

                return

            elif guess < number:

              await ctx.send("Your guess was __Smaller__ than the original number :pensive:\n*Hint :- The original number is __Greater__ than your guess!*\n```Chances Remaining :- 1```")

              response = await self.client.wait_for('message', check=check)

              guess = int(response.content)

              if guess > number:

                await ctx.send(f"Your guess was __Greater__ than the original number :pensive:\nThe Original number was {number}")

                return

              elif guess < number:

                await ctx.send(f"Your guess was __Smaller__ than the original number :pensive:\nThe Original number was {number}")

                return

              else:

                await ctx.send(f'Bingo! You guessed it!:tada:\nThe number was {number}')

                return

            else:

              await ctx.send(f'Bingo! You guessed it!:tada:\nThe number was {number}')

              return

            

        else:

            await ctx.send(f'Bingo! You guessed it!:tada:\nThe number was {number}')

            return

def setup(client):

  client.add_cog(games(client))
