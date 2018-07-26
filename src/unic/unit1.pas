unit Unit1;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, FileUtil, Forms, Controls, Graphics, Dialogs, StdCtrls;

type

  { TForm1 }

  TForm1 = class(TForm)
    Button1: TButton;
    Memo1: TMemo;
    Memo2: TMemo;
    procedure Button1Click(Sender: TObject);
  private

  public

  end;

var
  Form1:TForm1;
  i,j:Integer;
  s,s11,s12,s21,s22:String;
  list,unic,rus:TStringList;
  t1,t2:UnicodeString;
  flag:Boolean;
  //re:TRegExpr;

implementation

{$R *.lfm}

{ TForm1 }

procedure TForm1.Button1Click(Sender: TObject);
begin
  list:=TStringList.Create;
  unic:=TStringList.Create;
  rus:=TStringList.Create;
  for i:=0 to Memo1.Lines.Count-1 do
  begin
    ExtractStrings(['#'],[],pchar(Memo1.Lines.Strings[i]),list);
    //ShowMessage(list[0]);ShowMessage(list[1]);ShowMessage(list[2]);
    s:=AnsiLowerCase(list[0]+'#'+list[1]);
    flag:=False;
    for  j:=0 to unic.Count-1 do if AnsiLowerCase(unic[j])=s then begin flag:=True;break;end;
    if flag=False then
    begin
      unic.Add(AnsiLowerCase(s));
      rus.Append(list[2]);
    end;
    list.Clear;
end;
  Memo1.Clear;
  for i:=0 to unic.Count-1 do
  begin
   Memo1.Lines.add(unic[i]+' '+rus[i]);// AnsiLowerCase()
    end;
  for i:=0 to Memo1.Lines.Count-1 do
  begin
    ExtractStrings(['#'],[],pchar(Memo1.Lines.Strings[i]),list);
    flag:=False;
    for j:=0 to memo2.Lines.Count do begin
     if Memo2.Lines.Strings[j]=list[0]+':'+list[0]+'                type;' then begin flag:=True;break;end;
    end;
    if flag=False then
    Memo2.Lines.Add(list[0]+':'+list[0]+'                type;');
    list.Clear;
  end;


end;
end.

