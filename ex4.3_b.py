emp_info={
    'David':{
        'bossOf':['Ken','Nick'],
        'has':'staff'
    },
    'Ken':{
        'has':'Department'
    },
    'Nick':{
        'has':'Department'
    },
    'Department':{
        'has':'staff'
    },
}

print(list(emp_info.keys())[0],"is boss of",emp_info['David']['bossOf'])
