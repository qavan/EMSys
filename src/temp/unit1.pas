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
  var i:Integer;
    s,s11,s12,s21,s22:String;
    list:TStringList;
    t1,t2:UnicodeString;
    re:TRegExpr;


implementation

{$R *.lfm}

{ TForm1 }

procedure TForm1.Button1Click(Sender: TObject);
begin
  re:=TRegExpr.Create('(\/\*)');
  list:=TStringList.Create;
  for i:=0 to Memo1.Lines.Count-1 do
  if ((Pos(' ',Memo1.Lines.Strings[i])<>0)or(Pos('%',Memo1.Lines.Strings[i])<>0))
  or
  (
  (Pos('ө',Memo1.Lines.Strings[i])<>0) or (Pos('ә',Memo1.Lines.Strings[i])<>0) or (Pos('җ',Memo1.Lines.Strings[i])<>0) or
  (Pos('Ө',Memo1.Lines.Strings[i])<>0) or (Pos('Ә',Memo1.Lines.Strings[i])<>0) or (Pos('Җ',Memo1.Lines.Strings[i])<>0)
  or (Pos('ү',Memo1.Lines.Strings[i])<>0) or (Pos('ң',Memo1.Lines.Strings[i])<>0)  or
  (Pos('Ү',Memo1.Lines.Strings[i])<>0)
  )

  then begin end
  else
  begin
    s:=Memo1.Lines.Strings[i];
    ExtractStrings(['#'],[],pchar(s),list);
    //if list.LineBreak;
    s11:='';//list[0][1];
    s12:=list[0];//AnsiLowerCase(Copy(list[0],2,Length(list[0])));
    s21:='';//list[1][1];
    s22:=list[1];//AnsiLowerCase(Copy(list[1],2,Length(list[1])));
  {if re.Exec(Memo2.Lines.Strings[i])=false then
  begin
    Memo3.Lines.Add(s11+s12+':'+s11+s12+'     temp;!""');
  end;}
    Memo4.Lines.Add(s21+s22+':'+s21+s22+'     temp;!""');
    //<e><p><l>Ямалтдинов<s n="np"/><s n="ant"/><s n="temp"/></l><r>Ямалтдинов<s n="np"/><s n="cog"/><s n="temp"/></r></p></e>

    Memo5.Lines.Add('<e><p><l>'+s21+s22+'<s n="np"/><s n="ant"/><s n="temp"/></l><r>'+s11+s12+'<s n="np"/><s n="ant"/><s n="temp"/></r></p></e>');
    list.Clear;
  end;
end;

end.

