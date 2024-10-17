const button1 = document.querySelector("#button1");

function readFile(file) {
    return new Promise((resolve, reject) => {
        const reader = new FileReader();
        reader.onload = () => resolve(reader.result);
        reader.onerror = reject;
        reader.readAsText(file);
    });
}
button1.addEventListener('click',processFiles);

async function processFiles()
 {
    const inputFile = document.querySelector("#inputFile").files[0];
    const optabFile = document.querySelector("#optabFile").files[0];
    if(!inputFile || !optabFile)
    {
        document.querySelector("#output").textContent="error proccessing the files...";

    };
    try
    {
        // read the file 
        const inputcontent = await readFile(inputFile);
        const optabcontent = await readFile(optabFile);
        //pass 1 and pass 2
        const output=pass1andpass2(inputcontent,optabcontent)
        //output
        document.querySelector("#output").textContent=output;

    }
    catch(err)
    {
        console.error(err);
        document.querySelector("#output").textContent="error loading the files...";
    }
}


function pass1andpass2(inputcontent,optabcontent)
{
    const optab={};
    optabcontent.split('\n').forEach(line => {
        const [menomonic,opcode] = line.trim().split(/\s+/);
        if(opcode && menomonic){
            optab[menomonic]=opcode;
        }
    });
    const lines=inputcontent.split('\n')
    const symtab={};
    let locationcounter=0;
    const startingaddress=parseInt(lines[0].split(/\s+/)[2],16);
    locationcounter=startingaddress;

    const intermediateCode=[];
    const parts=line.trim().split(/\s+/);

    if(parts.length ==4)
    {
        const [address,label,instruction,operand]= parts;
    
        if(label!='_')
        {
            symtab[label]=locationcounter.toString(16).toUpperCase;
        }
        intermediateCode.push({address,instruction,operand})
        if(optab[instruction])
        {
            locationcounter=locationcounter+3;
        }
        else if(optab[instruction]='BYTE')
        {
            locationcounter+=operand.length - 3;
        }
        else if(optab[instruction]='WORD')
        {
            locationcounter+=3;
        }
        else if(optab[instruction]='RESB')
        {
            locationcounter+=parseInt(operand);
        }
        else if(optab[instruction]='RESW')
        {
            locationcounter+=3 * parseInt(operand);
        }
        
    }
    //pass[2]
    let mcode='pass 2: \n';
    intermediateCode.forEach(line=>
    { 
        const {address,instruction,operand}=line;
        let opcode = optab[instruction] || '';
        let operandaddress =  symtab[operand] ||operand ||'';

        if (instruction === 'BYTE') {
            const byteValue = operand.slice(2, -1); // Extract byte content
            mcode += `${address} ${byteValue}\n`;
        } else if (instruction === 'WORD') {
            const wordValue = parseInt(operand, 10).toString(16).padStart(6, '0').toUpperCase();
            mcode += `${address} ${wordValue}\n`;
        } else if (opcode) {
            mcode += `${address} ${opcode} ${operandaddress}\n`;
        }

    } );

    let output='Pass 1 Symbol Table:\n';
    for(const [label,address] of Object.entries(symtab) )
    {
        output+=`${label}: ${address}\n`;
    }

     output += '\n' + mcode;
    return output;

}