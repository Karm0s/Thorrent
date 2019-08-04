# TODO: decode the bin hashes into ascii hashes.
import asyncio
import yabencode
import os
import datetime


class MetaInfo:

    def __init__(self, torrent_path):
        self.torrent_path = torrent_path
        self.decoded_data = self.get_decoded_data(torrent_path)

        # First we get the announce url and convert it to a string
        if 'announce' in self.decoded_data:
            self.announce = self.decoded_data['announce'].decode('utf-8')
        else:
            self.print_error('"announce" key not found.')

        # Here we get the info's content
        if not ('info' in self.decoded_data):
            self.print_error('"info" key not found.')
        # Check if it is a multiple files torrent
        if 'files' in self.decoded_data['info']:
            print("here mate")
            raise RuntimeError('Multi-file torrents are not supported for the moment.')
        else:

            if 'md5sum' in self.decoded_data['info']:
                self.md5sum = self.decoded_data['info']['md5sum']
            else:
                self.md5sum = 0

            self.name = self.decoded_data['info']['name']
            self.length = self.decoded_data['info']['length']
            self.piece_length = self.decoded_data['info']['piece length']
            self.pieces = self.decoded_data['info']['pieces']
        if 'announce list' in self.decoded_data:
            self.announce_list = self.decoded_data['announce list']
        else:
            self.announce_list = None
        if 'creation date' in self.decoded_data:
            self.creation_date = datetime.datetime.fromtimestamp(int(self.decoded_data['creation date'])).strftime('%c')
        else:
            self.creation_date = None
        if 'comment' in self.decoded_data:
            self.comment = self.decoded_data['comment']    
        else:
            self.comment = None
        if 'created by' in self.decoded_data:
            self.creator = self.decoded_data['created by']
        else:
            self.creator = None

    def get_decoded_data(self, torrent_path):
        with open(torrent_path, mode='rb') as f:
            try:
                return yabencode.decode(f.read())

            except yabencode.MalformedBencodeException as e:
                self.print_error(e)

    def print_error(self, message):
        print(f'Error in torrent file: {message}')
        exit()
