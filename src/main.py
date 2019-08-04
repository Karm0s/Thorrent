import asyncio
import argparse
from metaInfo import MetaInfo

# main function
async def main():
    metainfo = MetaInfo('drstone.torrent')
    #metainfo2 = MetaInfo('drstone.torrent')
    
    print("Announce :"+str(metainfo.announce)+"\n")
    print("Announce list: "+str(metainfo.announce_list)+"\n")
    print("Comment: "+str(metainfo.comment)+"\n")
    print("Creation date: "+str(metainfo.creation_date)+"\n")
    print("Creator: "+str(metainfo.creator)+"\n")
    print("Lenght: "+str(metainfo.length)+"\n")
    print("md5sum: "+str(metainfo.md5sum)+"\n")
    print("Name: "+str(metainfo.name)+"\n")
    print("Piece lenght: "+str(metainfo.piece_length)+"\n")

    await asyncio.sleep(1)


if __name__ == '__main__':
    asyncio.run(main())
