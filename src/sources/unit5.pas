unit Unit5;

{$mode objfpc}{$H+}

interface

uses
  Classes, SysUtils, FileUtil, Forms, Controls, Graphics, Dialogs, StdCtrls,RegExpr;

type

  { TForm5 }

  TForm5 = class(TForm)
    Button1: TButton;
    CheckBox1: TCheckBox;
    Memo1: TMemo;
    Memo2: TMemo;
    procedure Button1Click(Sender: TObject);
  private

  public

  end;

var
  Form5: TForm5;
  i:Integer;

implementation

{$R *.lfm}

{ TForm5 }

procedure TForm5.Button1Click(Sender: TObject);
var re:TRegExpr;list:TStringList;s:string;
begin
  list:=TStringList.Create;
  re:=TRegExpr.Create('[һүәҗө]'); //әөүҗңh
  for i:=1 to Memo1.Lines.Count do
  begin
    {if re.Exec(Memo1.Lines.Strings[i]) then begin
      s:=  Memo1.Lines.Strings[i];
      Memo1.Lines.Strings[i]:='!'+Memo1.Lines.Strings[i];
      ExtractStrings([':'],  ['-',' '], pchar(s), list);
      s:='<e><p><l>'+list[0]+'<s n="np"/><s n="cog"/></l><r>'+list[0]+'<s n="np"/><s n="cog"/></r></p></e>';
      s:='<!-- '+s+' -->' ;
      Memo2.Lines.Add(s);
      // <e><p><l>Барбадос<s n="np"/><s n="cog"/></l><r>Барбадос<s n="np"/><s n="cog"/></r></p></e>
    end
    else  }
     begin
      s:=  Memo1.Lines.Strings[i];
      ExtractStrings([':'],  ['-',' '], pchar(s), list);
      s:='<e><p><l>'+list[0]+'<s n="np"/><s n="cog"/></l><r>'+list[0]+'<s n="np"/><s n="cog"/></r></p></e>';
      Memo2.Lines.Add(s);
     end;
     list.Clear;
  end;
end;

end.

