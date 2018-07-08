unit Unit2;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, FileUtil, Forms, Controls, Graphics, Dialogs, StdCtrls,
  ExtCtrls;

type

  { TForm2 }

  TForm2 = class(TForm)
    Button1: TButton;
    ComboBox1: TComboBox;
    Memo1: TMemo;
    Memo2: TMemo;
    Memo3: TMemo;
    Memo4: TMemo;
    Memo5: TMemo;
    RadioGroup1: TRadioGroup;
    procedure Button1Click(Sender: TObject);
    procedure FormClose(Sender: TObject; var CloseAction: TCloseAction);
    procedure FormShow(Sender: TObject);
  private

  public

  end;

var
  Form2: TForm2;
  s:string;
  i:integer;
  j:integer;
  t1,t1lr,t1rl,types,t2,t3,t0:string;
implementation
       uses unit1;
{$R *.lfm}

{ TForm2 }
function R(var s:string):string;//Replacer
begin
  s:=s.Replace('ç','ҫ');s:=s.Replace('ĕ','ӗ'); s:=s.Replace('ă','ӑ');s:=s.Replace('ÿ','ӳ');
  R:=s;
end;
procedure RD(const stringList : TStringList) ;//RemoveDuplicates
var
  buffer: TStringList;
  cnt: Integer;
begin
  stringList.Sort;
  buffer := TStringList.Create;
  try
    buffer.Sorted := True;
    buffer.Duplicates := dupIgnore;
    buffer.BeginUpdate;
    for cnt := 0 to stringList.Count - 1 do
      buffer.Add(stringList[cnt]) ;
    buffer.EndUpdate;
    stringList.Assign(buffer) ;
  finally
    FreeandNil(buffer) ;
  end;
end;

procedure TYPE1();
var
  list,templist:TStringList;
  typeof,prev,current:string;
begin
    list:=TStringList.Create;
   for i:=0 to Form2.Memo1.Lines.Count-1 do
     begin
       s:=Form2.Memo1.Lines.Strings[i];
       ExtractStrings([':'],  ['-',' '], pchar(s), list);
       if list.Count=4 then begin
       s:=list[2];s:=R(s);
       //s:=s.Replace('ç','ҫ');s:=s.Replace('ĕ','ӗ'); s:=s.Replace('ă','ӑ');s:=s.Replace('ÿ','ӳ');
       Form2.Memo2.Lines.Add(list[3]+':'+list[0]+':'+s);
       end;
       list.Clear;
     end;
   templist:=TStringList.Create;
   templist.AddStrings(Form2.memo2.lines);
   templist.Sort;
   RD(templist) ;
   Form2.memo2.Clear;
  Form2.memo2.Lines.AddStrings(templist);
end;

procedure TYPE2();
var
    list,templist:TStringList;
    typeof,prev,current:string;
  begin
      list:=TStringList.Create;
     for i:=0 to Form2.Memo1.Lines.Count-1 do
       begin
         s:=Form2.Memo1.Lines.Strings[i];
         ExtractStrings([':'],  ['-',' '], pchar(s), list);
         if list.Count=3 then begin
         s:=list[2];s:=R(s);
         //s:=s.Replace('ç','ҫ');s:=s.Replace('ĕ','ӗ'); s:=s.Replace('ă','ӑ');s:=s.Replace('ÿ','ӳ');
         Form2.Memo2.Lines.Add(list[0]+':'+s);
         end;
         list.Clear;
       end;
     templist:=TStringList.Create;
     templist.AddStrings(Form2.memo2.lines);
     templist.Sort;
     RD(templist) ;
     Form2.memo2.Clear;
    Form2.memo2.Lines.AddStrings(templist);
end;

procedure TForm2.FormClose(Sender: TObject; var CloseAction: TCloseAction);
begin
    //Form1.Visible:=True;
end;

procedure TForm2.Button1Click(Sender: TObject);
begin
  if RadioGroup1.ItemIndex=0 then begin
  TYPE1();Memo2.Color:=clMoneyGreen;
  end
  else begin
  TYPE2();Memo2.Color:=clRed;
  end;
end;

procedure TForm2.FormShow(Sender: TObject);
begin
  t1:='<e><p><l>';
  t1lr:='<e r="LR"><p><l>';
  t1rl:='<e r="RL"><p><l>';
  types:='HERE-IS-PLACE-FOR-TYPE';
  t2:='</l><r>';
  t3:='</r></p></e>';
end;

end.

