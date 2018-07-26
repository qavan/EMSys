unit Unit1;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, FileUtil, Forms, Controls, Graphics, Dialogs, StdCtrls,RegExpr;

type

  { TForm1 }

  TForm1 = class(TForm)
    Button1: TButton;
    Memo1: TMemo;
    Memo2: TMemo;
    Memo3: TMemo;
    Memo4: TMemo;
    Memo5: TMemo;
    procedure Button1Click(Sender: TObject);
  private

  public

  end;

var
  Form1: TForm1;
  i:integer;
  s,s11,s12,s21,s22:String;
  list:TStringList;
  t1,t2:UnicodeString;
  re:TRegExpr;

implementation

{$R *.lfm}

{ TForm1 }

procedure TForm1.Button1Click(Sender: TObject);
begin
  list:=TStringList.Create;
  for i:=0 to Memo1.Lines.Count-1 do
  begin
    ExtractStrings(['#'],[],pchar(Memo1.Lines.Strings[i]),list);
    //ShowMessage(list[1]);
    if (Pos(' ',Memo1.Lines.Strings[i])=0)  then if (Pos('-',Memo1.Lines.Strings[i])=0) then
    if (Pos('*',Memo2.Lines.Strings[i])<>0) then
    if (Pos(' ',Memo2.Lines.Strings[i])=0) then if (Pos('#',Memo2.Lines.Strings[i])=0)  then if (Pos('-',Memo2.Lines.Strings[i])=0) then
    begin
      memo5.Lines.Add('<e><p><l>'+list[1]+'<s n="v"/><s n="tv"/></l><r>'+list[0]+'<s n="v"/><s n="tv"/></r></p></e>'+'<!--'+list[2]+'-->');
    end;
    list.Clear;
  end;
end;

end.

